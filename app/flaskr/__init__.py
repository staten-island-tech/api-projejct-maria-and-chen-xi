import os
import requests
import time

from flask import Flask, render_template
anime_name = 'Cowboy Bebop'
app = Flask(__name__)

def search(name):
    count = 0
    for x in name:
        
        if x == '%':
            Xcount = count
            for thing in name:
                if thing == '2':
                    if Xcount==count+1:
                        name[count] = ''
                        name[Xcount] = '+'
                Xcount = Xcount+1
        count = count+1
    print(name)
    return name


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>/')
def animepage(name):
    # final_name = name.replace("%20", " ")
    # print(final_name)
    # anime = requests.get(f"https://api.jikan.moe/v4/anime/{final_name}/full")
    # if '200' in str(anime):
    #     return render_template('animePage.html', anime=anime)
    # else:
    #     return render_template('error.html')
    print(name)
    final_name = name.replace("%20", "+")

    print(final_name)
    return(render_template('one piece.html', name=final_name))
    # if final_name == "One Piece":
    #     return render_template("one piece.html")
    # else:
    #     return render_template('error.html')

