import csv
from src.song import Song
class Data_loader :
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
        self.track_list.append(new_song)
        with open(self.file_path , "a", encoding="utf-8" , newline="") as file :
            w = csv.writer(file)
            w.writerow([new_song.track_id,new_song.artists,new_song.album_name,new_song.track_name,new_song.popularity,new_song.duration_ms,new_song.explicit,new_song.danceability,new_song.energy,new_song.key,
                        new_song.loudness,new_song.mode,new_song.speechiness,new_song.acousticness,new_song.instrumentalness,new_song.liveness,new_song.valence,new_song.tempo,new_song.time_signature,new_song.track_genre])
    def reset_data(self):
        self.track_list = []
        self.read_data()
    def save_data(self):
        out_path = "data/cleaned_dataset.csv"
        fnames = [
            "track_id", "artists", "album_name", "track_name", "popularity", 
            "duration_ms", "explicit", "danceability", "energy", "key", 
            "loudness", "mode", "speechiness", "acousticness", "instrumentalness", 
            "liveness", "valence", "tempo", "time_signature", "track_genre"
        ]
        with open(out_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fnames)
            for song in self.track_list:
                writer.writerow([
                    song.track_id, song.artists, song.album_name, song.track_name, song.popularity,
                    song.duration_ms, song.explicit, song.danceability, song.energy, song.key,
                    song.loudness, song.mode, song.speechiness, song.acousticness, song.instrumentalness,
                    song.liveness, song.valence, song.tempo, song.time_signature, song.track_genre
                ])
        print(f"sucsessfully saved in '{out_path}' file . ")