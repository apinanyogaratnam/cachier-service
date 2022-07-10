FROM python:3.10.4-alpine

LABEL org.opencontainers.image.source=https://github.com/apinanyogaratnam/cachier-service

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
