from flask import Flask, render_template,request,redirect,url_for
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "My Application"
heading = "Hello World"
client = MongoClient("mongodb://192.168.1.110:27017")
db = client.mymongodb
todos = db.todo


@app.route("/")
def home_page():
	online_users = todos.find()
	return render_template("index.html",t=title,h=heading)

if __name__ == '__main__':
	app.run()
