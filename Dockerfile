FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8-slim
WORKDIR /code
COPY . .
COPY --from=builder /usr/local /usr/local
COPY . .
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
ENV MONGO_URI='mongodb://192.168.1.109:27017/nischal'
EXPOSE 5000
CMD ["flask", "run"]
