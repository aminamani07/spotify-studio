import csv
from song import Song
class data_loader :
    def __init__(self , file_path):
        self.file_path = file_path
        self.track_list = []
    def read_data(self):
        with open(self.file_path , "r", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for r in reader :
                s_ob = Song(track_id=r["track_id"], artists=r["artists"], album_name=r["album_name"], track_name=r["track_name"], popularity=r["popularity"], duration_ms=r["duration_ms"],
explicit=r["explicit"], danceability=r["danceability"], energy=r["energy"], key=r["key"], loudness=r["loudness"], mode=r["mode"], speechiness=r["speechiness"],
acousticness=r["acousticness"], instrumentalness=r["instrumentalness"], liveness=r["liveness"], valence=r["valence"], tempo=r["tempo"], time_signature=r["time_signature"],
track_genre=r["track_genre"])
                self.track_list.append(s_ob)
    def append_track(self , new_song):
        pass