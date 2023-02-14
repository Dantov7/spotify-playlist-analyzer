import requests


class Playlist :
    def __init__(self, base_url, headers, playlist_id):

        self.__playlist_endpoint = 'playlists/'+playlist_id
        self.__response_playlist = requests.get(base_url+self.__playlist_endpoint, headers=headers)
        self.__total_tracks = len(self.__response_playlist.json()['tracks']['items'])
        
        self.__params_items  = {
            'limit' : self.__total_tracks
        }         
        
        self.__response_playlist_items = requests.get(base_url+self.__playlist_endpoint+'/tracks', headers=headers, params=self.__params_items)

        self.__params_ids  = {
            "ids" : self.tracks_id_extraction()[1]
            }   
        
        self.__response_audio_features = requests.get(base_url+'audio-features', headers=headers, params=self.__params_ids)
        

    def tracks_id_extraction(self):
        tracks_id = []
        for i in range(self.__total_tracks):            
            track_id = self.__response_playlist_items.json()['items'][i]['track']['id']
            tracks_id.append(track_id)
            tracks_id_string = ",".join(tracks_id)
        # regreso una lista de ids y un string con todos los ids separados por coma
        return tracks_id, tracks_id_string

    
    def get_cover_image(self):
        response_image = requests.get(self.__response_playlist.json()['images'][0]['url'])
        with open ('cover.jpg', 'wb') as file:
            file.write(response_image.content)

    def get_followers(self):
        followers = self.__response_playlist.json()["followers"]["total"]
        return followers
    

    def tracks_extraction(self):
        tracks_list = []
        for i in range(self.__total_tracks):
            track = self.__response_playlist_items.json()['items'][i]['track']['name']
            tracks_list.append(track)
        #tracks_list =  (f'{i+1}- {track}, Artista: {artist}')
        return tracks_list      


    def tracks_artists_extraction(self):
        artists = []
        for i in range(self.__total_tracks):
            artist = self.__response_playlist_items.json()['items'][i]['track']['artists'][0]['name']
            artists.append(artist)
        return artists

    # Se ingresa un string con la lista de ids, documentado en la API. Robado de daniela
    def get_features (self):
        
        features = ["tempo","acousticness","danceability","energy","instrumentalness","liveness","loudness","valence"]
        list_tempo = []
        list_acousticness = []
        list_danceability = []
        list_energy = []
        list_instrumentalness = []
        list_liveness = []
        list_loudness = []
        list_valence = []

        for i in range(self.__total_tracks):
            for key in features:
                data = self.__response_audio_features.json()["audio_features"][i][key]
                
                if key == "tempo":
                    list_tempo.append(data)

                elif key == "acousticness":
                    list_acousticness.append(data)

                elif key == "danceability":
                    list_danceability.append(data)                
                
                elif key == "energy":
                    list_energy.append(data)
                
                elif key == "instrumentalness":
                    list_instrumentalness.append(data)
                
                elif key == "liveness":
                    list_liveness.append(data)
                
                elif key == "loudness":
                    list_loudness.append(data)
                
                elif key == "valence":
                    list_valence.append(data)          

        features_tracks = {

            "tempo": self.__get_average(list_tempo),
            "acousticness": self.__get_average(list_acousticness),
            "danceability": self.__get_average(list_danceability),
            "energy": self.__get_average(list_energy),
            "instrumentalness": self.__get_average(list_instrumentalness),
            "liveness": self.__get_average(list_liveness),
            "loudness": self.__get_average(list_loudness),
            "valence": self.__get_average(list_valence)
        }
        print (features_tracks)
        return features_tracks


    def __get_average(self,list):
        
        suma = 0
        for i in list:
            suma += i 
        average = round(suma/len(list), 2)
        return average
    
    def get_playlist_name(self):
        return self.__response_playlist.json()["name"]
    
    def get_playlist_description(self):
        return self.__response_playlist.json()["description"]

    """Función para obtener el response original para troubleshooting"""
    
    def get_churro(self):
        return self.__response_playlist




