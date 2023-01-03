import os
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    variable = requests.get("https://api.jikan.moe/v4/anime/21/full")
    return render_template('index.html', variable=variable)

