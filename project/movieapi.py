
from urllib.request import urlcleanup
from click import secho
import requests
from decouple import config

#getting enviroment variable
key = config('mdbKey')
    
# funciton to extract Name of series or movie 
def name(value):
    if "original_name" in value:
            return value['original_name']
    elif "original_title" in value:
            return value['original_title']
    elif "name" in value:
            return value['name']
    else:
            return None

class pack():
    def __init__(self):
        pass
    
    #return backposter of most most popular show or movie of today for home page
    def home(self):
        url = f"https://api.themoviedb.org/3/trending/all/day?api_key={key}"
        r = requests.get(url)
        poster = r.json()['results'][0]['backdrop_path']
        poster= f"https://image.tmdb.org/t/p/original{poster}" #creating full url from path
        return poster

    def discover(self,type, page=1):
        if type == "tv":
            url=f"https://api.themoviedb.org/3/discover/tv?api_key={key}&language=en-US&sort_by=popularity.desc&page={page}&timezone=America%2FNew_York&include_null_first_air_dates=false&with_watch_monetization_types=flatrate&with_status=0&with_type=0"
            series = True
        else:
            url = "https://api.themoviedb.org/3/discover/movie?api_key={}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={}&with_watch_monetization_types=flatrate".format(key,page)
            series = False
        r = requests.get(url)
        try:
            list = []
            data = r.json()['results']
            for i in data:
                id = i['id']
                title = name(i)
                poster= f"https://www.themoviedb.org/t/p/w220_and_h330_face/{i['backdrop_path']}" #creating full url from path
                dict ={
                "id":id,
                "title": title,
                "poster": poster,
                "series" :series,
                }
                list.append(dict)
        except Exception as e:
            dict = {
                "error": e
            }
            list.append(dict)
        finally:
            return list
    
    def trending(self, time="day", media="movie", page=1):
        # media -> which kind of media {movie, tvshow, all}
        # time -> trending today or this week
        url = f"https://api.themoviedb.org/3/trending/{media}/{time}?api_key={key}&page={page}"
        if media == "tv":
            series = True
        else:
            series = False
        r = requests.get(url)
        try:
            list = []
            data = r.json()['results']
            for i in data:
                id = i['id']
                title = name(i)
                poster= f"https://www.themoviedb.org/t/p/w220_and_h330_face/{i['backdrop_path']}" #creating full url from path
                dict ={
                        "id":id,
                        "title": title,
                        "poster": poster,
                        "series" :series,
                    }
                list.append(dict)
        except Exception as e:
            dict = {
                        "error": e
                    }
            list.append(dict)
        finally:
            return list

    def search(self,query=None, page=1, adult="true"):
        url = "https://api.themoviedb.org/3/search/multi?api_key={}&language=en-US&query={}&page={}&include_adult={}".format(key, query, page,adult)          
        r = requests.get(url)
        try:
            list = []
            data = r.json()['results']
            for i in data:
                type = i["media_type"]
                if not type == 'person':
                    path=i['poster_path']
                    if path == None:
                        continue

                    id = i['id']
                    title = name(i)
                    poster= f"https://www.themoviedb.org/t/p/w220_and_h330_face/{i['poster_path']}" #creating full url from path
                elif type == "person":
                    id = i['id']
                    path=i['profile_path']
                    if path == None:
                        continue
                    poster= f"https://www.themoviedb.org/t/p/w220_and_h330_face/{path}" #creating full url from path
                    title = name(i)

                dict ={
                        "id":id,
                        "title": title,
                        "poster": poster,
                        "type" : type,
                    }
                list.append(dict)
        except Exception as e:
            dict = {
                        "error": e
                    }
            list.append(dict)
        finally:
            return list

    def get(self, id, series):
        if series == True:
            url = f"https://api.themoviedb.org/3/tv/{id}?api_key={key}&language=en-US"
        else:
            url = f"https://api.themoviedb.org/3/movie/{id}?api_key={key}&language=en-US" 
        print(url)