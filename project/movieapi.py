from ast import DictComp
from turtle import back
import requests
from decouple import config

#getting enviroment variable
key = config('mdbKey')

class movies():
    def __init__(self):
        pass

    def discover(self, page):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}&with_watch_monetization_types=flatrate"
        r = requests.get(url).json()['results']
        movieList =[]
        for p in r:
            id = p['id']
            poster = f"https://image.tmdb.org/t/p/w220_and_h330_face{p['poster_path']}" #converting the image path into full url 
            if 'original_title' in p:
                title = p['original_title']
            elif 'original_name' in p:
                title = p['original_name']
            else:
                title = 'Null'
            dict = {
                'title': title,
                "id": id,
                "poster": poster
            }
            movieList.append(dict)
        return movieList

    
    def trendingToday(self):
        url = f"https://api.themoviedb.org/3/trending/all/day?api_key={key}"
        popular = requests.get(url).json()['results']
        movieList =[]
        for p in popular:
            id = p['id']
            poster = f"https://image.tmdb.org/t/p/w220_and_h330_face{p['poster_path']}" #converting the image path into full url 
            if 'original_title' in p:
                title = p['original_title']
            elif 'original_name' in p:
                title = p['original_name']
            else:
                title = 'Null'
            dict = {
                'title': title,
                "id": id,
                "poster": poster
            }
            movieList.append(dict)
        return movieList

    def trendingWeek(self):
        url = f"https://api.themoviedb.org/3/trending/all/week?api_key={key}"
        popular = requests.get(url).json()['results']
        movieList =[]
        for p in popular:
            id = p['id']
            poster = f"https://image.tmdb.org/t/p/w220_and_h330_face{p['poster_path']}" #converting the image path into full url 
            if 'original_title' in p:
                title = p['original_title']
            elif 'original_name' in p:
                title = p['original_name']
            else:
                title = 'Null'
            dict = {
                'title': title,
                "id": id,
                "poster": poster
            }
            movieList.append(dict)
        return movieList

    def get_by_id(self,id):
        url = f'https://api.themoviedb.org/3/movie/{id}?api_key={key}'
        p = requests.get(url).json()
        id = p['id']
        poster = f"https://image.tmdb.org/t/p/w220_and_h330_face{p['poster_path']}" #converting the image path into full url 
        back = f"https://image.tmdb.org/t/p/w220_and_h330_face{p['backdrop_path']}"
        description = p['overview']
        production_company = p['production_companies']
        release_date = p['release_date']
        revenue = p['revenue']
        genres = p['genres']
        budget =p['budget']
        imdb = f"https://www.imdb.com/title/{p['imdb_id']}/"
        spoken_languages = p['spoken_languages']
        if 'original_title' in p:
                title = p['original_title']
        elif 'original_name' in p:
                title = p['original_name']
        else:
                title = 'Null'
        production_countries = p['production_countries']
        dict = {
                'title': title,
                "id": id,
                "poster": poster,
                "back_poster": back,
                "description": description,
                "production_company": production_company,
                "production_countries": production_countries,
                "release_date": release_date,
                "revenue":revenue,
                "genres" : genres,
                "budget" : budget,
                "imdb" : imdb,
                "spoken_languages" : spoken_languages
            }
        return dict
