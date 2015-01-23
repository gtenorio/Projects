from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) #app has instance of flask
app.config.from_object('config') #tells flask to read config file
db = SQLAlchemy(app)

from app import views, models #put at the end because views depends on app package (line 3)
