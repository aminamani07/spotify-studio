import matplotlib as pb
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
