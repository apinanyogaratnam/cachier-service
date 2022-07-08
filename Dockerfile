FROM python:3.10.4-alpine

LABEL org.opencontainers.image.source=https://github.com/apinanyogaratnam/REPO

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
