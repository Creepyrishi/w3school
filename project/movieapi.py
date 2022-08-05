from tkinter import simpledialog
import requests
from decouple import config

#getting enviroment variable
key = config('mdbKey')

nullImg = "https://th.bing.com/th/id/R.76801db49ff2ab1c1c744116023144ca?rik=zINagHQZSPOU%2fw&riu=http%3a%2f%2fwww.selikoff.net%2fblog-files%2fnull-value.gif&ehk=cNq4qNJX05TgPMcuWYCuj%2f18PfoXbgy0X1B7lN8m1eU%3d&risl=&pid=ImgRaw&r=0"

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

#Function to identify the id is of which media type
def findType(id):
    type = None
    if requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={key}").status_code == 200:
        type = "movie"
    elif requests.get(f"https://api.themoviedb.org/3/tv/{id}?api_key={key}").status_code == 200:
        type = 'tv'
    return type
#main pack
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
                        "series": True if findType(id) =="tv" else False,
                    }
                list.append(dict)
                print(dict)
        except Exception as e:
            dict = {
                        "error": e
                    }
            list.append(dict)
        finally:
            return list

    def get(self, id, series,):
        similarList = []
        if series == True:
            detailUrl = f"https://api.themoviedb.org/3/tv/{id}?api_key={key}&language=en-US"
            trailerUrl = f"https://api.themoviedb.org/3/tv/{id}/videos?api_key={key}&language=en-US"
            castCrewUrl = f"https://api.themoviedb.org/3/tv/{id}/credits?api_key={key}&language=en-US"
            similarURl = f"https://api.themoviedb.org/3/tv/{id}/similar?api_key={key}&language=en-US&page=1"

        else:
            detailUrl = f"https://api.themoviedb.org/3/movie/{id}?api_key={key}&language=en-US"
            trailerUrl = f"https://api.themoviedb.org/3/movie/{id}/videos?api_key={key}&language=en-US"
            castCrewUrl = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key={key}&language=en-US"
            similarURl = f"https://api.themoviedb.org/3/movie/{id}/similar?api_key={key}&language=en-US&page=1"


        # making requests  

        imgUrl = f"https://api.themoviedb.org/3/movie/{id}/images?api_key={key}&language=en-US"
        detail = requests.get(detailUrl).json()
        images = requests.get(imgUrl).json()
        trailers = requests.get(trailerUrl).json()['results']
        casts = requests.get(castCrewUrl).json()['cast']
        crews = requests.get(castCrewUrl).json()['crew']
        similar = requests.get(similarURl).json()['results']
        
        #production company
        productionCompany = []
        for company in detail["production_companies"]:
            if company['logo_path'] != None:
                tempList1 = {'id' : company['id'],
                            'name': company['name'], 
                            'logo': f"https://image.tmdb.org/t/p/original{company['logo_path']}"
                            }
                productionCompany.append(tempList1)
                tempList1= {}

        #production country
        productionCountry = []
        for country in detail["production_countries"]:
            productionCountry.append(company['name'])

        #trailer
        trailerList = []
        for trailer in trailers:
            if trailer['type'] == 'Trailer' and trailer['site'] == "YouTube":
                trailerList.append(trailer['key'])
        #genre
        genreList=[]
        for item in detail['genres']:
            genreList.append({'id' :str(item['id']), 
                            'name' : item['name']})

        #crew and cast
        castList = []
        for cast in casts:
            if cast['profile_path'] != None:
                castList.append(
                    {
                        "id":cast['id'],
                        "character":cast['character'],
                        "name": cast['name'],
                        "picture": f"https://www.themoviedb.org/t/p/w220_and_h330_face/{cast['profile_path']}" ,
                    }
                )
        crewList = []
        for crew in crews:
            if cast['profile_path'] != None:
                crewList.append(
                    {
                        "id":crew['id'],
                        "job": crew['job'],
                        "department": crew['department'],
                        "name": crew['name'],
                        "picture": f"https://www.themoviedb.org/t/p/w220_and_h330_face/{cast['profile_path']}" 
                    }
                )

        #for only series
        seasonList = []
        if series == True:
            for season in detail['seasons']:
                seasonList.append({"id" : season['id'],
                                "title" :  name(detail) + " - " +name(season),
                                "seasonNumber": season['season_number'],
                                "episodeCount" : season['episode_count'],
                                "poster": f"https://www.themoviedb.org/t/p/w220_and_h330_face/{season['poster_path']}" if detail[
                                    'poster_path'] != None else nullImg
                })

        else:
            seasons= []

        #for similar
        for i in similar:
            similarList.append(
                {
                "id": i['id'],
                "title": name(i),
                "poster": f"https://www.themoviedb.org/t/p/w220_and_h330_face/{i['backdrop_path']}",
                "series": series,
            }
            )


        #details common for both movies and series
        dict ={
                "id":id,
                "title": name(detail),
                "backdrop": f"https://image.tmdb.org/t/p/original{detail['backdrop_path']}" if detail['backdrop_path'] != None else nullImg,
                "poster": f"https://www.themoviedb.org/t/p/w220_and_h330_face/{detail['poster_path']}" if detail['poster_path'] != None else nullImg,
                "trailerIdList": trailerList,
                "genres": genreList,
                "overview": detail['overview'],
                "language": detail['spoken_languages'],
                "series": series,
                "company":productionCompany,
                "country": productionCountry,
                "cast" :castList,
                "crew" :crewList,
                "seasons": seasonList,
                'similar': similarList,
                }

        return dict