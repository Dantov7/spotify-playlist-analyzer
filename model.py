from playlist import Playlist
from auth import Auth
from user_stats import User


class Model():
    def __init__(self):
        self.__user_data = None
        self.__base_url = 'https://api.spotify.com/v1/'
        self.__headers = None
        self.__feature_tracks = {}
        self.__playlist_name = None
        self.__playlist_description = None
        

    def login(self):
        auth = Auth()
        auth.generate_token()    # use it only for the first time
        token = auth.get_token()
        headers = {
            'Authorization': f'Bearer {token}',
            "Accept": "application/json"
        }
        self.__headers = headers
        
        #Capturo la información del usuario
        user_stats = User(self.__base_url, headers)
        self.__user_data = user_stats.get_user_data()
        self.__top_10_artists = user_stats.top10_artist()
        self.__top_5_genres = user_stats.top_5_genres()
        self.__top_10_tracks = user_stats.top_10_tracks()
        return self.__user_data


    def playlist_analysis(self, playlist_id):
        
        playlist = Playlist(self.__base_url, self.__headers,  playlist_id)
        self.__feature_tracks = playlist.get_features()
        playlist.get_cover_image()
        self.__playlist_name = playlist.get_playlist_name()
        self.__playlist_description = playlist.get_playlist_description()
        return self.__feature_tracks


    """Funciones para enviar infor a los otros modulos"""
    def get_user_data(self):
        return self.__user_data
    
    def get_top_10_artists(self):
        return self.__top_10_artists
    
    def get_top_5_genres(self):
        return self.__top_5_genres
    
    def get_top_10_tracks(self):
        return self.__top_10_tracks

    def get_playlist_name(self):
        return self.__playlist_name

    def get_playlist_description(self):
        return self.__playlist_description


