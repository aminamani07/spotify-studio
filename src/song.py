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
        #use property
        self.valence = valence
        self.popularity = popularity
        self.danceability = danceability
        self.energy = energy
    @property
    def popularity(self):
        return self._popularity
    @popularity.setter
    def popularity(self , value):
        if value is None or value == "":
            self._popularity = None 
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
            self._danceability = None
            return
        if not (0 <= float(value) <= 1.0):
            raise ValueError(f"Danceability error : value '{value}' must be between 0.0 and 1.0 . ")
        self._danceability = float(value)
    @property
    def energy(self):
        return self._energy
    @energy.setter
    def energy(self , value):
        if value is None or value == "":
            self._energy = None 
            return
        if not (0.0 <= float(value) <= 1.0):
            raise ValueError(f"Energy error : value '{value}' must be between 0.0 and 1.0 . ")
        self._energy = float(value)
    @property
    def valence(self):
        return self._valence
    @valence.setter
    def valence(self , value):
        if value is None or value == "":
            self._valence = None
            return
        if not (0.0 <= float(value) <= 1.0):
            raise ValueError(f"Valence error : value '{value}' must be between 0.0 and 1.0 . ")
        self._valence = float(value)
    @property
    def duration_ms(self):
        return self._duration_ms
    @duration_ms.setter
    def duration_ms(self, value):
        if value is None or value == "":
            self._duration_ms = None
            return
        val = float(value)
        if val <= 0:
            self._duration_ms = None
        else:
            self._duration_ms = val

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        if value is None or value == "":
            self._key = None
            return
        val = int(float(value))
        if not (0 <= val <= 11):
            self._key = None
        else:
            self._key = val

    @property
    def loudness(self):
        return self._loudness
    @loudness.setter
    def loudness(self, value):
        if value is None or value == "":
            self._loudness = None
            return
        val = float(value)
        if not (-60.0 <= val <= 0.0):
            self._loudness = None
        else:
            self._loudness = val

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, value):
        if value is None or value == "":
            self._mode = None
            return
        val = int(float(value))
        if val not in [0, 1]:
            self._mode = None
        else:
            self._mode = val

    @property
    def speechiness(self):
        return self._speechiness
    @speechiness.setter
    def speechiness(self, value):
        if value is None or value == "":
            self._speechiness = None
            return
        val = float(value)
        if not (0.0 <= val <= 1.0):
            self._speechiness = None
        else:
            self._speechiness = val

    @property
    def acousticness(self):
        return self._acousticness
    @acousticness.setter
    def acousticness(self, value):
        if value is None or value == "":
            self._acousticness = None
            return
        val = float(value)
        if not (0.0 <= val <= 1.0):
            self._acousticness = None
        else:
            self._acousticness = val

    @property
    def instrumentalness(self):
        return self._instrumentalness
    @instrumentalness.setter
    def instrumentalness(self, value):
        if value is None or value == "":
            self._instrumentalness = None
            return
        val = float(value)
        if not (0.0 <= val <= 1.0):
            self._instrumentalness = None
        else:
            self._instrumentalness = val

    @property
    def liveness(self):
        return self._liveness
    @liveness.setter
    def liveness(self, value):
        if value is None or value == "":
            self._liveness = None
            return
        val = float(value)
        if not (0.0 <= val <= 1.0):
            self._liveness = None
        else:
            self._liveness = val

    @property
    def tempo(self):
        return self._tempo
    @tempo.setter
    def tempo(self, value):
        if value is None or value == "":
            self._tempo = None
            return
        val = float(value)
        if val <= 0.0:
            self._tempo = None
        else:
            self._tempo = val

    @property
    def time_signature(self):
        return self._time_signature
    @time_signature.setter
    def time_signature(self, value):
        if value is None or value == "":
            self._time_signature = None
            return
        val = int(float(value))
        if not (3 <= val <= 7):
            self._time_signature = None
        else:
            self._time_signature = val


