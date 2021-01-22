FROM python:3.8
WORKDIR /code
COPY . .
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
ENV MONGO_URI='mongodb://192.168.1.109:27017/nischal'
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]
