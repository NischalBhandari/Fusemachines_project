from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
	user_collection = mongo.db.hero
	user_collection.insert({'name': 'Anthony'})
	return '<h1>Added a user</h1>'
