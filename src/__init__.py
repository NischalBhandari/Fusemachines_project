import os
from .extensions import mongo
from flask import Flask
from .main import main

def create_app(config_object='src.settings'):
	app = Flask(__name__)

	app.config.from_object(config_object)
	print(app)
	mongo.init_app(app)
	app.register_blueprint(main)
	return app
