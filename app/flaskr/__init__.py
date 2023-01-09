import os
import requests

from flask import Flask, render_template

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def anime(name):
    variable = requests.get(f"https://api.jikan.moe/v4/anime/{name}/full")
    # print(str(variable.status_code()))
    # # if variable.status_code() != 200:
    # #     return render_template('error.html')
    # # else:
    return render_template('animePage.html', variable=variable)

