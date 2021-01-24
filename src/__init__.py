import os
from .extensions import mongo
from flask import Flask
from .main import main

def create_app(config_object='src.settings'):
	app = Flask(__name__)
	app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD']+ '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
	#app.config.from_object(config_object)
	print(app)
	mongo.init_app(app)
	app.register_blueprint(main)
	return app
