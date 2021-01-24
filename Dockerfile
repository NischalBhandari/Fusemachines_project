FROM python:3.8 AS builder
WORKDIR /code
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /code
COPY . .
COPY --from=builder /root/.local/bin /root/.local
COPY ./src .
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
ENV MONGO_URI='mongodb://192.168.1.109:27017/nischal'
EXPOSE 5000
CMD ["flask", "run"]
