from app import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'jef'}

    teams = [
        {'name': 'Paris SG', 'rank': 1},
        {'name': 'SM Caen',  'rank': 12},
        {'name': 'OM',       'rank': 4},
        {'name': 'OL',       'rank': 9},
    ]
    matchs = [
        {'team_A': teams[0], 'team_B': teams[1]},
        {'team_A': teams[2], 'team_B': teams[3]}
    ]

    return render_template('index.html', user = user, matchs = matchs, title = "Home")
