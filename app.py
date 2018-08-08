import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
  return json.dumps("This is an unofficial bard catalog.")

@app.route('/<rc_number>')
def rc_number(rc_number):
  return json.dumps({"rc_number": rc_number})