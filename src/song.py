class Song :
    def __init__(self , id , track_id, artists, album_name, track_name, popularity, duration_ms,
                explicit, danceability, energy, key, loudness, mode, speechiness,
                acousticness, instrumentalness, liveness, valence, tempo, time_signature,
                track_genre):
        self.id = id
        self.track_id = track_id
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.key = key
        self.loudness = loudness
        self.mode  = mode
        self.tempo = tempo
        self.time_signature = time_signature
        self.track_genre = track_genre
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        #use property
        self.popularity = popularity
        self.danceability = danceability
        self.energy = energy
    @property
    def popularity(self):
        return self._popularity
    @popularity.setter
    def popularity(self , value):
        if value is None or value == "":
            self._popularity = 0.0 
            return
        if not (0 <= float(value) <= 100):
            raise ValueError(f"popularity error : value '{value}' must be between 0 and 100 . ")
        self._popularity = float(value)
    @property
    def danceability(self):
        return self._danceability
    @danceability.setter
    def danceability(self , value):
        if value is None or value == "":
            self._danceability = 0.0 
            return
        if not (0 <= float(value) <= 100):
            raise ValueError(f"Danceability error : value '{value}' must be between 0.0 and 1.0 . ")
        self._danceability = float(value)
    @property
    def energy(self):
        return self._energy
    @energy.setter
    def energy(self , value):
        if value is None or value == "":
            self._energy = 0.0 
            return
        if not (0.0 <= float(value) <= 1.0):
            raise ValueError(f"Energy error : value '{value}' must be between 0.0 and 1.0 . ")
        self._energy = float(value)


