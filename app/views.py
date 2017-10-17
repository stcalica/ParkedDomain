from app import app
from flask import request
from flask import render_template
import json, requests

@app.route('/', methods = [ 'GET'])
@app.route('/index', methods = [ 'GET'])
def index():
	return render_template('index.html', title='Galileo Gear')
