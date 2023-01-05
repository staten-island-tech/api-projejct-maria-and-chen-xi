import os
import requests
import time

from flask import Flask, render_template
anime_name = 'Cowboy Bebop'
app = Flask(__name__)
 
@app.route('/')
def home():
    count = 0 
    while count != 30:
        time.sleep(0.34)
        anime = requests.get(f'https://api.jikan.moe/v4/anime/{count}/full')
        print(anime)
        print(anime.json())
        if '200' in str(anime):
            print(anime.json()['data']['title'])
            if anime_name in anime.json()['data']['title']:
                return render_template('index.html', anime=anime)
            # if anime_name in anime.json()['data']['title_japanese']:
            #     return render_template('index.html', anime=anime)
        count = count + 1

    return render_template('error.html')
        
    full = requests.get('http://api.jikan.moe/v4/anime')
    return render_template('index.html', full=full)

@app.route('/<int:name>')
def anime(name):
    anime = requests.get(f"https://api.jikan.moe/v4/anime/{name}/full")
    return render_template('animePage.html', anime=anime)

