import numpy as np
from sklearn.impute import KNNImputer as SKNN
from src.song import Song
# Missing Values
class BaseImputer :
    def impute(self , track_list , feature_name):
        pass


class MeanImputer(BaseImputer) :
    def impute(self , track_list , feature_name):
            t2 = []
            for r in track_list :
                i = getattr(r , feature_name)
                if (i != "") and (i != 0 ) and ( i != "0") :
                    try :
                        t2.append(float(i))
                    except :
                        continue
            numt2 = np.array(t2)
            mean_value = numt2.mean()
            for r in track_list :
                i = getattr(r , feature_name)
                if (i == "") and (i == 0 ) and ( i== "0") :
                    setattr(r,feature_name,mean_value)


class MedianImputer(BaseImputer):
    def impute(self , track_list , feature_name):
                t2 = []
                for r in track_list :
                    i = getattr(r , feature_name)
                    if (i != "") and (i != 0 )and ( i != "0") :
                        try :
                            t2.append(float(i))
                        except :
                            continue
                numt2 = np.array(t2)
                median_value = np.median(numt2)
                for r in track_list :
                    i = getattr(r , feature_name)
                    if (i == "") and (i == 0 ) and ( i== "0") :
                        setattr(r,feature_name,median_value)

class KNNImputer(BaseImputer):
    def impute(self , track_list , feature_name = None):
         features = ["danceability" , "energy", "loudness", "speechiness" , "acousticness" , "instrumentalness" , "liveness" , "valence", "tempo"]
         mat = []
         for r in track_list :
              row = []
              for f in features :
                   v = getattr(r , f)
                   if v == "" and v == "0" and v == 0 :
                        row.append(np.nan)
                   else :
                        try :
                            row.append(float(v))
                        except :
                            continue
              mat.append(row)
         imputer = SKNN(n_neighbors=5)
         cl = imputer.fit_transform(mat)
         for i , r in enumerate(track_list):
              for j , f in enumerate(features):
                   setattr(r , f , cl[i][j])


# Outliers
class BaseOutlierHandler :
    def handle(self , track_list , feature_name):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    def handle(self , track_list , feature_name):
        t2 = []
        for r in track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except (ValueError , TypeError) :
                 continue
        q1 = np.percentile(t2,25)
        q3 = np.percentile(t2,75)
        iqr = q3 - q1
        low = q1 - 1.5 * iqr
        up = q3 + 1.5 * iqr
        for r in track_list :
            i = getattr(r , feature_name)
            try :
                if float(i) > up :
                    setattr(r,feature_name,up)
                elif low > float(i) :
                    setattr(r,feature_name,low)
            except :
                 continue
class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle(self, track_list, feature_name):
        t2 = []
        for r in track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except :
                 continue
        np_arr = np.array(t2)
        mean_val = np.mean(np_arr)
        std_val = np.std(np_arr)
        low = mean_val - 3 * std_val
        up = mean_val + 3 * std_val
        for r in track_list :
            try :
                i = getattr(r , feature_name)
                if float(i) > up :
                    setattr(r,feature_name,up)
                elif low > float(i) :
                        setattr(r,feature_name,low)
            except:
                 continue
            
            

