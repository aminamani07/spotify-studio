class song :
    def __init__(self , track_id, artists, album_name, track_name, popularity, duration_ms,
explicit, danceability, energy, key, loudness, mode, speechiness,
acousticness, instrumentalness, liveness, valence, tempo, time_signature,
track_genre):
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
        #use property
        self.popularity = popularity
        self.danceability = danceability
        self.energy = energy
        self.speechiness = speechiness
        self.acoustisness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        