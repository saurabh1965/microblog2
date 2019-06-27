from flask import render_template 
from app import app
@app.route('/')
@app.route('/h2')
def h2():
	return render_template('h2.html',title='home')

