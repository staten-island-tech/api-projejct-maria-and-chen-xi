import os
import requests
import time

from flask import Flask, render_template
# anime_name = 'Cowboy Bebop'
app = Flask(__name__)

# def search(name):
#     count = 0
#     for x in name:
        
#         if x == '%':
#             Xcount = count
#             for thing in name:
#                 if thing == '2':
#                     if Xcount==count+1:
#                         name[count] = ''
#                         name[Xcount] = '+'
#                 Xcount = Xcount+1
#         count = count+1
#     print(name)
#     return name


@app.route('/')
def home():
    top = requests.get('https://api.jikan.moe/v4/top/anime')
    genres = requests.get('https://api.jikan.moe/v4/genres/anime')
    return render_template('index.html', top=top, genres=genres)

@app.route('/<name>/')
def animepage(name):
    final_name = name.replace("%20", "+")
    anime = requests.get(f'https://api.jikan.moe/v4/anime?q={final_name}&sfw')
    print(anime.json())
    try: 
        if anime.json()['status'] == 404:
            return render_template('error.html', status=anime.json()['status'], message=anime.json()['message'])
    except KeyError:
        return(render_template('animePage.html', anime=anime))
