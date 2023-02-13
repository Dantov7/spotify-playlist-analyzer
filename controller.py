import requests
import json

from collections import Counter
from user_stats import User


class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__connect_signals()
        self.__user_data = None
        self.__playlist_id = None
        self.__playlist_features = None

    def __connect_signals(self):
        self.__view.login_button.clicked.connect(self.login)
        self.__view.analyze_button.clicked.connect(self.handle_playlist_input)
        

    def login(self):
        self.__model.login()
        self.__view.login_exitoso.setText("Login exitoso!")
        self.__user_data = self.__model.get_user_data()
        self.__top_10_artists = self.__model.get_top_10_artists()
        self.__top_5_genres = self.__model.get_top_5_genres()
        self.__top_10_tracks = self.__model.get_top_10_tracks()
        self.change_login_labels()
        self.change_favorites()


    def change_login_labels(self):
        username = "Bienvenido " + self.__user_data[0]
        followers = "Actualmente tienes " + str(self.__user_data[1]) + " followers"
        self.__view.bienvenida_user.setText(username)
        self.__view.seguidores.setText(followers)


    def change_favorites(self):
        """Creo una lista con las variables.setText de la GUI para iterar"""
        artists_dict = [self.__view.artists_1.setText, self.__view.artists_2.setText, self.__view.artists_3.setText, self.__view.artists_4.setText, self.__view.artists_5.setText]

        songs_dict = [self.__view.songs_1.setText, self.__view.songs_2.setText, self.__view.songs_3.setText, self.__view.songs_4.setText, self.__view.songs_5.setText]

        genres_dict = [self.__view.genre_1.setText, self.__view.genre_2.setText, self.__view.genre_3.setText, self.__view.genre_4.setText, self.__view.genre_5.setText]

        for i in range(5):
            artists_dict[i](self.__top_10_artists[i])
            songs_dict[i](self.__top_10_tracks[i][0])
            genres_dict[i](self.__top_5_genres[i])
    

    def handle_playlist_input(self):        
        playlist = self.__view.playlist_link_box.text()
        self.__playlist_id = playlist.strip('https://open.spotify.com/playlist/')
        print(self.__playlist_id)
        self.analyze_playlist()
        self.change_playlist_features()
        self.change_cover()
        return self.__playlist_id

    def analyze_playlist(self):
        self.__playlist_features = self.__model.playlist_analysis(self.__playlist_id)
        print (self.__playlist_features)
    
    def change_playlist_features(self):
        """Creo diccionarios con las variables.setText de la GUI para iterar"""
        features_btn_list = [self.__view.tempo_value.setText,
                        self.__view.acousticness_value.setText, 
                        self.__view.danceability_value.setText, 
                        self.__view.energy_value.setText, 
                        self.__view.instrumentalness_value.setText, 
                        self.__view.liveness_value.setText, 
                        self.__view.loudness_value.setText, 
                        self.__view.valence_value.setText
        ]
        features_list = [
            "tempo",
            "acousticness",
            "danceability",
            "energy",
            "instrumentalness",
            "liveness",
            "loudness",
            "valence"
        ]
        for i in range(8):
            features_btn_list[i](str(self.__playlist_features[features_list[i]]))

    def change_cover(self):
        self.__view.cover_img("cover.jpg")
            
            



