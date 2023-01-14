from flask import Flask, render_template
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://edwardma33:Delaware33@cluster0.hp6ofba.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def home_page():
    dashboard = mongo.db.tasks.find({})

    return dashboard




