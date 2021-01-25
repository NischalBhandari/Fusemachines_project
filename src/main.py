from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from .extensions import mongo
main = Blueprint('main', __name__)


@main.route('/')
def index():
	todos = mongo.db.hero
	saved_todos = todos.find()
	return render_template('index.html', todos=saved_todos)

@main.route('/add', methods=['POST'])
def add_todo():
	todos = mongo.db.hero
	new_todo = request.form.get('new-todo')
	todos.insert_one({'text' : new_todo, 'complete' : False})
	return redirect(url_for('main.index'))

@main.route('/complete/<oid>')
def complete(oid):
	todos = mongo.db.hero
	todo_item = todos.find_one({'_id': ObjectId(oid)})
	todo_item['complete'] = True
	todos.save(todo_item)
	return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
	todos = mongo.db.hero
	todos.delete_many({'complete' : True})
	return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
	todos = mongo.db.hero
	todos.delete_many({})
	return redirect(url_for('main.index'))
