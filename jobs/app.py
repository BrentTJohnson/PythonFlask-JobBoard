import sqlite3
from flask import Flask, render_template, g
PATH = 'db/jobs.sqlite3'


app = Flask(__name__)


@route('/jobs')
@route('/')
def jobs():
	return render_template('index.html')
