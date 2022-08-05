from flask import Flask, redirect, render_template, url_for, request
from movieapi import *
import random
import requests

app = Flask(__name__)

# creating instance for movie api 
pack = pack()

#globals
type = "day"
media = "movie"


@app.route("/")
@app.route("/home")
def home():
    poster = pack.home()
    return render_template("index.html", poster = poster)

# discover
@app.route("/discover", methods=['GET','POST'])
def discover():
    global type
    global media    
    try:
        media = request.form['media']
        page = 1
    except:
        pass
    try:
        page = int(request.args.get('page'))
    except:
        page = 1
    if page > 1:
        previousPage = page - 1
    else:
        previousPage = 1
    nextPage = page + 1

    data = pack.discover(type=media,page=page)
    return render_template("discover.html", list =data, page=page , previousPage = previousPage, nextPage = nextPage, time = type.upper(), type = media.upper())

#trending
@app.route("/trending", methods=['GET','POST'])
def trending():
    global type
    global media
    #for time{{  in first request it will set to day }}
    try:
        type = request.form['time']
        page = 1
    except:
        pass
    #for media type{{  in first request it will set to movie }}
    try:
        media = request.form['media']
        page = 1
    except:    
        pass
    try:
        page = int(request.args.get('page'))
    except:
        page = 1
    if page > 1:
        previousPage = page - 1
    else:
        previousPage = 1
    nextPage = page + 1

    data = pack.trending(time=type,media=media,page=page)
    return render_template("trending.html", list =data, page=page , previousPage = previousPage, nextPage = nextPage,time= type.upper(), type = media.upper())
#search
@app.route("/search", methods=['GET','POST'])
def search():
    query = request.form['Search']
    page=1
    adult='false'
    data = pack.search(query, page, adult)
    return render_template("search.html", list = data, query= query)

#get
@app.route("/get", methods=['GET','POST'])
def get():
    get = request.form['get']
    type, id = get.split("/")
    if type == "False":
        type = False
    else:   
        type = True
    data = pack.get(id = int(id), series = type,)
    #for no trailers
    try:
        trailerId = random.choice(data['trailerIdList'])
    except:
        trailerId = ''
    return render_template(
        "get.html", 
        dict = data,
        backdrop = data['backdrop'],
        poster = data['poster'],
        trailerId=trailerId
    )
# test
@app.route("/test")
def test():
    return redirect("/home", code=302)


#about
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": 
    app.run(debug=True, port=9999, host="localhost")