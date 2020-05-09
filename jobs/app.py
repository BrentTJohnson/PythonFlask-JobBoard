import sqlite3
from flask import Flask, render_template, g
PATH = 'db/jobs.sqlite3'


app = Flask(__name__)


@app.route('/jobs')
@app.route('/')
def jobs():
	return render_template('index.html')
