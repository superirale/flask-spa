from app import app, models
from flask import render_template


@app.route('/')
def index():
    "vue entry point"
    return render_template('home.html')
