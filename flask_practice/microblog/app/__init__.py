from flask import Flask

app = Flask(__name__) #app has instance of flask
app.config.from_object('config') #tells flask to read config file
from app import views #put at the end because views depends on app package (line 3)
