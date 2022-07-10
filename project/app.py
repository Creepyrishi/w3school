from struct import pack
from flask import Flask, render_template, url_for, request
import movieapi
app = Flask(__name__)

pack = movieapi.movies() #instance for api

pageNu = 1
# next page 
@app.route("/page+")
def nextPage():
    global pageNu
    pageNu +=1
    discover = pack.discover(pageNu)
    #gettng list of full trending and making it shot
    list =[] #movies trending today will add in this 
    reco = [] #movies trending this week will add in this

    for i in range(0,10):
        list.append(pack.trendingToday()[i])
        reco.append(pack.trendingWeek()[i])
    return render_template("index.html", list = list, reco = reco , discover = discover, page=pageNu)
#previous page
@app.route("/page-")
def previousPage():
    global pageNu
    pageNu -=1
    discover = pack.discover(pageNu)
    #gettng list of full trending and making it shot
    list =[] #movies trending today will add in this 
    reco = [] #movies trending this week will add in this

    for i in range(0,10):
        list.append(pack.trendingToday()[i])
        reco.append(pack.trendingWeek()[i])
    return render_template("index.html", list = list, reco = reco , discover = discover,  page=pageNu)

#home page
@app.route("/")
def home():
    global pageNu
    pageNu =1
    discover = pack.discover(pageNu)
    #gettng list of full trending and making it shot
    list =[] #movies trending today will add in this 
    reco = [] #movies trending this week will add in this

    for i in range(0,10):
        list.append(pack.trendingToday()[i])
        reco.append(pack.trendingWeek()[i])
    return render_template("index.html", list = list, reco = reco , discover = discover,  page=pageNu)

#trending page
@app.route("/trending")
def trending():
    return render_template("trending.html")

#latest page
@app.route("/latest")
def latest():
    return render_template("latest.html")

#search page
@app.route("/search")
def search():
    return render_template("search.html")


#working here
@app.route("/ShowMovie/<string:n>")
def show(n):
    r = pack.get_by_id(int(n))
    return render_template("showMovie.html", dict = r)



if __name__ == "__main__": 
    app.run(debug=True, port=9999)