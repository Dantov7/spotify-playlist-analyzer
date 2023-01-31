import requests
from collections import Counter

import json

class User:

    def __init__(self, base_url, headers):
        self.__base_url = base_url
        self.__headers = headers      
        self.__endpoint = 'me/top/'
        self.__params = {
        "limit" : "10",
        } 
        self.__response_top10_artists = requests.get(self.__base_url+self.__endpoint+"artists" , headers=self.__headers, params=self.__params)
        self.__response_top10_tracks = requests.get(self.__base_url+self.__endpoint+"tracks" , headers=self.__headers, params=self.__params)

        self.user_statistics = {"user_favorites":{"top_10_artists":self.top10_artist(), "Top_5_genres":self.top_5_genres(), "Top_10_tracks": self.top_10_tracks()}}

    #Opcional para mi GUI
    def get_user_data(self): #no necesita params , OPCIONAL
        endpoint = 'me/'
        response = requests.get(self.__base_url+endpoint, headers= self.__headers)
        username = response.json()['display_name']
        user_followers = response.json()['followers']['total']
        user_data = [username, user_followers]
        print (f'Bienvenido: { username }, actualmente tiene {user_followers} seguidores')
        return user_data


    def top10_artist(self):       
        top10_artists = []
        #print ("Tus Top 10 de artistas más escuchados es:")
        for i in range(10):
            artist = self.__response_top10_artists.json()['items'][i]['name']
            #print (f'{i+1}- {artist}')
            top10_artists.append(artist)
        return top10_artists
            

    def top_5_genres(self):
        total_genres = []
        #print ("Tus Top 5 de géneros más escuchados es:")
        for i in range(10):
            genre = self.__response_top10_artists.json()['items'][i]['genres']
            total_genres = total_genres + genre

        #uso Counter para contar los mas comunes en la lista total_genres
        count = Counter(total_genres)
        top_five_genres = []
        for genre, repeats in count.most_common(5):
            top_five_genres.append(genre)
        return top_five_genres
        

    def top_10_tracks(self):
        #print ("Tu Top 10 de canciones más escuchadas es:")
        top_10_tracks_with_artist = []  

        for i in range(10):
            song = self.__response_top10_tracks.json()['items'][i]['name']
            artist = self.__response_top10_tracks.json()['items'][i]['album']['artists'][0]['name']
            #print (f'{i+1}- {song}, Artista: {artist}')
            top_10_tracks_with_artist.append((song, artist))
        return top_10_tracks_with_artist #retorna tupla
        


    def save_json(data):
        with open ("churros.json","w") as file:
            json.dump(data, file)

    #save_json(aaa)