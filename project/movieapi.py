import requests
from decouple import config

#getting enviroment variable
key = config('mdbKey')

class movies():
    def __init__(self):
        pass


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
        r = requests.get(url).json()
        return r

