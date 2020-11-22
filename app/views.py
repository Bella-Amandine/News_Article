from flask import render_template
from app import app

@app.route("/")
def index():
    '''
    View root function that returns index and page and its data
    '''

    title = "Home - News Article"

    return render_template("index.html", title = title)