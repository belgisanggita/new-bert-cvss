## By Belgis Anggita

## Training Parameter Tuning
- Early stopping by val_loss (patience=2)
- Batch Size: 16  
- Learning Rate: 5e-5  
- Tokenizer/NLP Model: BERT-SMALL  

## Training, Validation, and Test Performance

| **Categories**             | **Train Loss** | **Train Acc** | **Val Loss** | **Val Acc** | **Test Loss** | **Test Acc** |
|----------------------------|----------------|---------------|--------------|-------------|---------------|--------------|
| **Attack Vector**          | 0.0179         | 0.9793        | 0.0176       | 0.9801      | 0.0185        | 0.9789       |
| **Attack Complexity**      | 0.0105         | 0.9863        | 0.0135       | 0.9836      | 0.0126        | 0.9841       |
| **Privileges Required**    | 0.0579         | 0.9232        | 0.1053       | 0.8851      | 0.1087        | 0.8860       |
| **User Interaction**       | 0.0341         | 0.9533        | 0.0369       | 0.9496      | 0.0360        | 0.9503       |
| **Scope**                  | 0.0210         | 0.9742        | 0.0212       | 0.9749      | 0.0207        | 0.9770       |
| **Confidentiality Impact** | 0.0645         | 0.9243        | 0.0913       | 0.9049      | 0.0891        | 0.9075       |
| **Integrity Impact**       | 0.0541         | 0.9371        | 0.1030       | 0.9032      | 0.1048        | 0.9031       |
| **Availability Impact**    | 0.0401         | 0.9485        | 0.0522       | 0.9411      | 0.0573        | 0.9376       |

## Test Metrics Summary

| **Categories**             | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1 Score** |
|----------------------------|--------------|-----------------------|---------------|------------|--------------|
| **Attack Vector**          | 0.9789       | 0.9789                | 0.9789        | 0.9789     | 0.9789       |
| **Attack Complexity**      | 0.9841       | 0.9841                | 0.9841        | 0.9841     | 0.9841       |
| **Privileges Required**    | 0.8860       | 0.8860                | 0.8855        | 0.8860     | 0.8857       |
| **User Interaction**       | 0.9503       | 0.9503                | 0.9504        | 0.9503     | 0.9503       |
| **Scope**                  | 0.9770       | 0.9770                | 0.9770        | 0.9770     | 0.9770       |
| **Confidentiality Impact** | 0.9075       | 0.9075                | 0.9075        | 0.9075     | 0.9073       |
| **Integrity Impact**       | 0.9031       | 0.9031                | 0.9034        | 0.9031     | 0.9032       |
| **Availability Impact**    | 0.9376       | 0.9376                | 0.9375        | 0.9376     | 0.9375       |



## Steps to Deploy
1. Clone repositories
    ```bash
    git clone https://github.com/belgisanggita/bert-cvss-prediction.git
    cd bert-cvss-prediction
    ```
2. Download the model without training
    - Download on **Releases** Section
    ![{38CAC19B-5B60-49D6-BCBE-15D61506DA48}](https://github.com/user-attachments/assets/28a5ec0d-a484-4bbc-bc45-758ffc090341)
    - Create "models" folder
        ```bash
        mkdir -p ./models
        ```
    - Extract all of the models from "models.zip" to "models/" folder 

3. Install Libraries
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
    ```
4. Run the model and the app
    ```bash
    python app.py
    ```

    
    
