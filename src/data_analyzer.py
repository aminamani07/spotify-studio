import matplotlib as pb
from collections import Counter
import numpy as np

class Dataanalyzer :
    def __init__(self , track_list):
        self.track_list = track_list
    def analyze_mean(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.mean(nt2)
        return return_val
    def analyze_median(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.median(nt2)
        return return_val
    def analyze_maximum(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.amax(nt2)
        return return_val
    def analyze_minimum(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.amin(nt2)
        return return_val
    def analyze_varians(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.var(nt2)
        return return_val
    def analyze_standarad_deviation(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        nt2 = np.array(t2)
        return_val = np.std(nt2)
        return return_val
    def analyze_mode(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        counter = Counter(t2)
        return_val = counter.most_common(1)[0][0]
        return return_val
    def filter_by_artist(self , atrists , n ):
        t2 = []
        for r in self.track_list :
            i = getattr(r , "artists")
            if i == atrists :
                t2.append(r)
        return t2[:n]
    def filter_by_genre(self , track_genre , n ):
        t2 = []
        for r in self.track_list :
            i = getattr(r , "track_genre")
            if i == track_genre :
                t2.append(r)
        return t2[:n]
    def get_top_tracks(self , feature, n):
        sorted_track = sorted(self.track_list , key = lambda track : float(getattr(track, feature)),reverse= True)
        return sorted_track[:n]
    def recommend(self , feature , n ,track):
        x = float(getattr(track , feature))
        sorted_track = sorted(self.track_list , key = lambda tracks : abs(float(getattr(tracks, feature)) - x))
        return sorted_track[1:n+1]

