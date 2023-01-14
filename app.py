from flask import Flask

from main.routes import main
from extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://edwardma33:Delaware33@cluster0.hp6ofba.mongodb.net/?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app