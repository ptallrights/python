#!/usr/bin/env python
from flask import Flask
from flask import request
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate,MigrateCommand
from flask import render_template
import redirect
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:redhat@localhost:3306/ops?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True

manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/host',methods=['GET','POST'])
def host():
	host_list  = Host.query.all()
	return render_template('host_list.html',host_list=host_list)

@app.route('/host_add',methods=['GET','POST'])
def host_add():

	if request.method == 'POST':
		hostname = request.form['hostname']
		ip = request.form['ip']
		port = request.form['port']
		postion = request.form['postion']
		description = request.form['description']
		host  = Host(hostname=hostname,ip=ip,port=port,postion=postion,description=description,user='')
		db.session.add(host)
		#db.session.commit()
		#return redirect('add_host.html')

        return render_template('add_host.html')

@app.route('/host_edit/<p_id>',methods=['GET','POST'])
def host_edit(p_id):
	host = Host.query.filter_by(id=p_id).first()
	if request.method == 'POST':
		hostname = request.form['hostname']
		ip = request.form['ip']
		port = request.form['port']
		postion = request.form['postion']
		description = request.form['description']
		host  = Host(hostname=hostname,ip=ip,port=port,postion=postion,description=description,user='')
		db.session.add(host)

	return render_template('edit_host.html',host=host)

@app.route('/host_del/<p_id>')
def host_del(p_id):
	host  = Host.query.filter_by(id=p_id).first()
	db.session.delete(host)
	return redirect(url_for('.host'))

@app.route('/show/<name>')
def show(name):
	namelist = ['tom','jerry','xiaowang']
	return render_template('show.html',namelist = namelist)

class Host(db.Model):
	__tablename__ = 'host'

	id = db.Column(db.Integer,primary_key=True)
	hostname = db.Column(db.String(100))
	ip = db.Column(db.String(50))
	port = db.Column(db.Integer)
	postion = db.Column(db.Integer)
	description = db.Column(db.Text)
	user = db.Column(db.String(20))


if __name__ == '__main__':
#        app.run(host='172.25.254.21',debug=True)
	manager.run()
