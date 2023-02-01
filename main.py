from collections import Counter
from playlist import Playlist
from auth import Auth
from user_stats import User
import json

base_url = 'https://api.spotify.com/v1/'
auth = Auth()
#auth.generate_token()    # use it only for the first time
token = auth.get_token()

headers = {
    'Authorization': f'Bearer {token}',
    "Accept": "application/json"
}

#Definir la playlist a analizar:
analyzed_playlist = 'https://open.spotify.com/playlist/37i9dQZF1DWWGFQLoP9qlv'
playlist_id = analyzed_playlist.strip('https://open.spotify.com/playlist/')

#Creo las instancias:
playlist = Playlist(base_url, headers, playlist_id)
user_stats = User(base_url, headers)




aa = user_stats.get_user_data()
bb = user_stats.top10_artist()
cc = user_stats.top_5_genres()
dd = user_stats.top_10_tracks()


#Funcion para guardar en json

def save_json(data):
    with open ("churros.json","w") as file:
        json.dump(data, file)

#save_json(aaa)



def save(*items):
    data={}
    with open ("Json.json","w") as file:
        
        for key in items:
            json.dump(data[key], file)