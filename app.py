from flask import Flask, render_template, request
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch.nn.functional as F
import pickle
from cvss import CVSS3

# Pilih device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Daftar metric
metrics = [
    'attack-vector', 'attack-complexity', 'privileges-required', 'user-interaction',
    'scope', 'confidentiality-impact', 'integrity-impact', 'availability-impact'
]

# Muat semua tokenizer, model, dan label
CVSS_classifiers = {}
print("Loading all tokenizers & models…")
for metric in metrics:
    model_dir = f'./models/{metric}'
    print(f" • {metric}: loading tokenizer…")
    tokenizer = BertTokenizerFast.from_pretrained(model_dir)
    tokenizer.model_max_length = 128

    print(f"            loading model…")
    model = BertForSequenceClassification.from_pretrained(model_dir)
    model.to(device)
    model.eval()

    fn = metric.replace('-', '_') + '_labels.pkl'
    label_path = f'labels/{fn}'
    print(f"            loading labels from {label_path}…")
    with open(label_path, 'rb') as f:
        labels = pickle.load(f)

    CVSS_classifiers[metric] = {
        'tokenizer': tokenizer,
        'model': model,
        'labels': labels
    }
    print(f"   ✓ {metric} ready")
print("All classifiers ready.\n")

def CVSS_vector_and_severity_predictor(vuln_desc: str):
    preds = {}
    for metric, assets in CVSS_classifiers.items():
        tok = assets['tokenizer'](
            vuln_desc,
            truncation=True,
            padding='max_length',
            max_length=assets['tokenizer'].model_max_length,
            return_tensors='pt'
        ).to(device)

        out = assets['model'](
            input_ids=tok['input_ids'],
            attention_mask=tok['attention_mask']
        )
        idx = torch.argmax(F.softmax(out.logits, dim=-1), dim=-1).item()
        preds[metric] = assets['labels'][idx]

    vector = (
        f"CVSS:3.1/AV:{preds['attack-vector'][0]}/"
        f"AC:{preds['attack-complexity'][0]}/"
        f"PR:{preds['privileges-required'][0]}/"
        f"UI:{preds['user-interaction'][0]}/"
        f"S:{preds['scope'][0]}/"
        f"C:{preds['confidentiality-impact'][0]}/"
        f"I:{preds['integrity-impact'][0]}/"
        f"A:{preds['availability-impact'][0]}"
    )
    preds['CVSS vector'] = vector

    c = CVSS3(vector)
    preds['severity score']  = c.scores()[0]
    preds['severity rating'] = c.severities()[0]
    return preds

# ===== FLASK APP =====
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return "All Models Running and Ready", 200

@app.route('/predict', methods=['POST'])
def predict():
    desc = request.form.get('description', '')
    results = CVSS_vector_and_severity_predictor(desc)
    return {
        "vector": results['CVSS vector'],
        "score": results['severity score'],
        "rating": results['severity rating'].upper()
    }, 200


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True,      # enable threads
        use_reloader=False
    )