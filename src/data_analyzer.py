from collections import Counter
import numpy as np

class Dataanalyzer :
    def __init__(self , track_list):
        self.track_list = track_list
    def analyze_mean(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except:
                continue
        nt2 = np.array(t2)
        return_val = np.mean(nt2)
        return f"Mean : {return_val}\n"
    def analyze_median(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                continue
        nt2 = np.array(t2)
        return_val = np.median(nt2)
        return f"Median : {return_val}\n"
    def analyze_maximum(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                continue
        nt2 = np.array(t2)
        return_val = np.amax(nt2)
        return f"Maximnm : {return_val}\n"
    def analyze_minimum(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except:
                continue
        nt2 = np.array(t2)
        return_val = np.amin(nt2)
        return f"Minimnm : {return_val}\n"
    def analyze_varians(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                continue
        nt2 = np.array(t2)
        return_val = np.var(nt2)
        return f"Varians : {return_val}\n"
    def analyze_standarad_deviation(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                continue
        nt2 = np.array(t2)
        return_val = np.std(nt2)
        return f"Standard Deviation : {return_val}\n"
    def analyze_mode(self , feature_name) :
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                continue
        counter = Counter(t2)
        return_val = counter.most_common(1)[0][0]
        return f"Mode : {return_val}\n"
    def filter_by_artist(self , atrists , n ):
        t2 = []
        for r in self.track_list :
            i = getattr(r , "artists")
            try :
                if i.lower() == atrists.lower() :
                    t2.append(r)
            except :
                continue
        return t2[:n]
    def filter_by_genre(self , track_genre , n ):
        t2 = []
        for r in self.track_list :
            i = getattr(r , "track_genre")
            try :
                if i == track_genre :
                    t2.append(r)
            except :
                continue
        return t2[:n]
    def get_top_tracks(self , feature, n):
        try :
            sorted_track = sorted(self.track_list , key = lambda track : float(getattr(track, feature)),reverse= True)
            return sorted_track[:n]
        except Exception as e :
            return e
    def recommend(self , feature , n ,track):
        try :
            x = float(getattr(track , feature))
            sorted_track = sorted(self.track_list , key = lambda tracks : abs(float(getattr(tracks, feature)) - x))
            return sorted_track[1:n+1]
        except Exception as e :
            return(e)

