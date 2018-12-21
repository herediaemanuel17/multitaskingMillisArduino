from flask import Flask
from flask import render_template
from database import Database
from flask_mysqldb import MySQL
from aux_pro import Process
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



app = Flask(__name__)


app.config['MYSQL_HOST', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DB', 'MYSQL_PORT' ] = 'localhost',  'example', 'example', 'db', '3306'
mysql = MySQL(app)
pro = Process()
db = Database()


@app.route('/')
def index():
	pro.start_process()
	last = db.get_last()
	return render_template('index.html', l = last)

@app.route('/cancelar')
def cancelar():
	last = db.get_last()
	pro.stop_process()
	return render_template('index.html', l = last)

if __name__ == '__main__':
	 app.run(debug = True, host='0.0.0.0', port=8888)
