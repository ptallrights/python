#!/usr/bin/env python
from flask import Flask
from flask import request
#from flask.ext.script import Manager

app = Flask(__name__)
#manager = Manager(app)

@app.route('/')
def index():
        return '<h1>hello wold</h1> %s' % request.headers.get('User_Agent'),200

@app.route('/show/<name>')
def show(name):
	if name == 'tom':
		return 'hello tom'
	else:
	        return 'go away'

if __name__ == '__main__':
        app.run(host='172.25.254.21',debug=True)
#	manager.run()
