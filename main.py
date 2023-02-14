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

"""
user_data = user_stats.get_user_data()
bb = user_stats.top10_artist()
cc = user_stats.top_5_genres()
dd = user_stats.top_10_tracks()
zz = playlist.get_features()
aa = playlist.get_churro()
kk = playlist.get_playlist_name()
ll = playlist.get_playlist_description()

print (kk)
print(ll)
"""

#Funcion para guardar en json
def save_json(data):
    data = json.loads(data.text)
    with open ("churros.json","w") as file:
        json.dump(data, file)
save_json(aa)


def save(*items):
    data={}
    with open ("Json.json","w") as file:
        
        for key in items:
            json.dump(data[key], file)
