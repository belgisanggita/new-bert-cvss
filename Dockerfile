FROM python:3.10.14-slim-bullseye
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 7860
CMD ["python", "app.py"]