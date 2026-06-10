import numpy as np
import sklearn as sk
from song import Song
# Missing Values
class BaseImputer :
    def impute(self , track_list , feature_name):
        pass


class MeanImputer(BaseImputer) :
    def impute(self , track_list , feature_name):
            t2 = []
            for r in track_list :
                i = getattr(r , feature_name)
                if (i != "") or (i != 0 )or ( i != "0") :
                    t2.append(float(i))
            numt2 = np.array(t2)
            mean_value = numt2.mean()
            for r in track_list :
                i = getattr(r , feature_name)
                if (i == "") or (i == 0 )or ( i== "0") :
                    setattr(r,feature_name,mean_value)



class MedianImputer(BaseImputer):
    pass

class KNNImputer(BaseImputer):
    pass


# Outliers
class BaseOutlierHandler :
    def handle(self , track_list , feature_name):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    pass

class ZScoreOutlierHandler(BaseOutlierHandler):
    pass