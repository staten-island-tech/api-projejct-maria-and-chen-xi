import os
import requests
import time

from flask import Flask, render_template
anime_name = 'Cowboy Bebop'
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:name>/')
def search(name):
    # final_name = name.replace("%20", " ")
    # print(final_name)
    # anime = requests.get(f"https://api.jikan.moe/v4/anime/{final_name}/full")
    # if '200' in str(anime):
    #     return render_template('animePage.html', anime=anime)
    # else:
    #     return render_template('error.html')
    print(name)
    final_name = name.replace("%20", " ")
    print(final_name)
    return(render_template('one piece.html', name=final_name))
    # if final_name == "One Piece":
    #     return render_template("one piece.html")
    # else:
    #     return render_template('error.html')

