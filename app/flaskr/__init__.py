import os
import requests

from flask import Flask, render_template

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:name>')
def anime(name):
    variable = requests.get(f"https://api.jikan.moe/v4/anime/{name}/full")
    return render_template('animePage.html', variable=variable)

