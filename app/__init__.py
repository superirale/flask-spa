from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, marshal, marshal_with, fields, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
app.secret_key = "eh4309jd"


#Load the views routes
from app import views

#Load api routes
from app import apis

# Load the config file
app.config.from_object('config')
