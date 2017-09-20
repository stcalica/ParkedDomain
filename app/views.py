from app import app
from flask import request
from flask import render_template
import json, requests

@app.route('/', methods = [ 'GET', 'POST'])
@app.route('/index', methods = [ 'GET', 'POST'])
def index():
	return render_template('index.html', title='Parked Domain')
