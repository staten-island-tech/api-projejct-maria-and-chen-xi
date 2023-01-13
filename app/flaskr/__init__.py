import requests

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    top = requests.get('https://api.jikan.moe/v4/top/anime')
    genres = requests.get('https://api.jikan.moe/v4/genres/anime')
    return render_template('index.html', top=top, genres=genres)

@app.route('/search:<search>/')
def search(search):
    results = requests.get(f'https://api.jikan.moe/v4/anime?q={search}&sfw')
    # print(anime.json())
    print(results.json()['pagination']['items']['count'])
    if results.json()['pagination']['items']['count'] == 0:
        return(render_template('noResults.html'))
    return(render_template('searchPage.html', results=results))

@app.route('/<id>/')
def animePage(id):
    anime = requests.get(f'https://api.jikan.moe/v4/anime/{id}/full')
    # print(anime.json())
    try: 
        if anime.json()['status'] == 404:
            return render_template('error.html', status=anime.json()['status'], message=anime.json()['message'])
    except KeyError:
        return(render_template('animePage.html', variable=anime))