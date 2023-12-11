from datetime import datetime, timedelta

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  years = (datetime.utcnow().date() - datetime(2017,1,1).date()).days // 365
  return render_template('home.html',
    years=years,
  )

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')
