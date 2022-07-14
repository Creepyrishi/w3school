
from flask import Flask, render_template, url_for, request
from movieapi import pack
app = Flask(__name__)

# creating instance for movie api 
pack = pack()

@app.route("/")
@app.route("/home")
def home():
    poster = pack.home()
    return render_template("index.html", poster = poster)

# discover
@app.route("/discover")
def discover():
    data = pack.discover(1)
    return render_template("discover.html", list =data, page=1)
#creatind two route to change page
page = 1
@app.route("/discover+")
def discoverPlus():
    global page
    page += 1
    data = pack.discover(page)
    return render_template("discover.html", list =data, page=page)

@app.route("/discover-")
def discoverMin():
    global page
    if page>2:
        page -= 1
    else:
        page=1
    data = pack.discover(page)
    return render_template("discover.html", list =data, page=page)
#trending
@app.route("/trending")
def trending():
    type='all'
    data = pack.trending(type)
    return render_template("trending.html", list =data)
#search
@app.route("/search", methods=['GET','POST'])
def search():
    query = request.form['Search']
    page=1
    adult='false'
    data = pack.search(query, page, adult)
    return render_template("search.html", list = data, query= query)
#about
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": 
    app.run(debug=True, port=9999)