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
	user_collection = mongo.db.users
	user_collection.insert({'name' : 'Nischal'})
	return '<h1>Added a user</h1>'

if __name__ == '__main__':
	app.run()
