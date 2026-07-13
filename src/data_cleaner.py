import numpy as np
from sklearn.impute import KNNImputer as SKNN
from src.song import Song

missing_report = []
outlier_report = []
missing_dict = {"track_id" : 0 , "artists" : 0 , "album_name" : 0 , "track_name" : 0 , "popularity" : 0 , "duration_ms" : 0 ,
"explicit": 0 , "danceability" : 0 , "energy" : 0 , "key" : 0 , "loudness" : 0 , "mode" :0, "speechiness" :0,
"acousticness" : 0 , "instrumentalness" : 0 , "liveness" : 0 , "valence" : 0 , "tempo" : 0 , "time_signature" : 0 ,
"track_genre" : 0}

# Missing Values
class BaseImputer :
    def impute(self , track_list , feature_name):
        pass


class MeanImputer(BaseImputer) :
    def impute(self , track_list , feature_name):
        if feature_name in ["explicit", "track_id" , "track_name" , "artists" , "album_name" , "track_genre"] :
            print("invalid feature..\n")
            return
        t2 = []
        for r in track_list :
            i = getattr(r , feature_name)
            if i not in ["" , " " , "None" ,  None]:
                try :
                    t2.append(float(i))
                except (ValueError , TypeError) :
                    continue
        numt2 = np.array(t2)
        mean_value = numt2.mean()
        for r in track_list :
            i = getattr(r , feature_name)
            if i in ["" , " " , "None" ,  None]:
                missing_dict[feature_name] += 1
                setattr(r,feature_name,mean_value)
                missing_report.append(f"track {track_list.index(r)+1} in first dataset : has missing value in feature : {feature_name} . and fixed it with mean and now it is : {mean_value} ")


class MedianImputer(BaseImputer):
    def impute(self , track_list , feature_name):
        if feature_name in ["explicit", "track_id" , "track_name" , "artists" , "album_name" , "track_genre"] :
            print("invalid feature..\n")
            return
        t2 = []
        for r in track_list :
            i = getattr(r , feature_name)
            if i not in ["" , " " , "None" ,  None] :
                try :
                    t2.append(float(i))
                except (ValueError , TypeError) :
                    continue
        numt2 = np.array(t2)
        median_value = np.median(numt2)
        for r in track_list :
            i = getattr(r , feature_name)
            if i in ["" , " " , "None" ,  None]:
                missing_dict[feature_name] += 1
                setattr(r,feature_name,median_value)
                missing_report.append(f"track {track_list.index(r)+1} in first dataset : has missing value in feature : {feature_name} . and fixed it with median and now it is : {median_value} ")

class KNNImputer(BaseImputer):
    def impute(self , track_list , feature_name = None):
         features = ["danceability" , "energy", "loudness", "speechiness" , "acousticness" , "instrumentalness" , "liveness" , "valence", "tempo"]
         mat = []
         for r in track_list :
              row = []
              for f in features :
                   v = getattr(r , f)
                   if v in ["" , " " , "None" ,  None] :
                        row.append(np.nan)
                        missing_report.append(f"track {track_list.index(r)+1} in first dataset : has missing value in feature : {f} . and fixed it with KNN (sklearn) . ")
                   else :
                        try :
                            row.append(float(v))
                        except (ValueError , TypeError) :
                            row.append(np.nan)
              mat.append(row)
        # add nomraliz part . (if we want)
        #from sklearn.preprocessing import MinMaxScaler
        #from sklearn.impute import KNNImputer as SKNN
        #from sklearn.metrics import accuracy_score
        #scaler = MinMaxScaler()
        #mat_scaled = scaler.fit_transform(mat) 
        #imputer = SKNN(n_neighbors=5)
        #cl_scaled = imputer.fit_transform(mat_scaled)
        #cl_original = scaler.inverse_transform(cl_scaled)
         imputer = SKNN(n_neighbors=5)
         cl = imputer.fit_transform(mat)
         for i , r in enumerate(track_list):
              for j , f in enumerate(features):
                   if getattr(r ,f) in ["" , " " , "None" , None]:
                       missing_dict[f] += 1
                   setattr(r , f , cl[i][j])
        # add accuracy part (if we want) .
        #has_nan = np.isnan(mat)
        #actual_labels = np.where(has_nan, 0, 1)
        #predicted_labels = np.ones_like(actual_labels)
        #acc = accuracy_score(actual_labels.flatten(), predicted_labels.flatten())
        #print(f"KNN Imputation Accuracy: {acc * 100:.2f}%")


# Outliers
class BaseOutlierHandler :
    def handle(self , track_list , feature_name):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    def handle(self , track_list , feature_name):
        if feature_name in ["explicit", "track_id" , "track_name" , "artists" , "album_name" , "track_genre"] :
             print("invalid feature..\n")
             return
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
        low = q1 - (1.5 * iqr)
        up = q3 + (1.5 * iqr)
        for r in track_list :
            i = getattr(r , feature_name)
            try :
                if float(i) > up :
                    setattr(r,feature_name,up)
                    outlier_report.append(f"track : {track_list.index(r) + 1} . has outlier value : {i} and we fixed it with iqroutlierhandler . after fixing : {up} . ")
                elif low > float(i) :
                    setattr(r,feature_name,low)
                    outlier_report.append(f"track : {track_list.index(r) + 1} . has outlier value : {i} and we fixed it with iqroutlierhandler . after fixing : {low} . ")
            except (ValueError , TypeError) :
                 continue
class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle(self, track_list, feature_name):
        if feature_name in ["explicit", "track_id" , "track_name" , "artists" , "album_name" , "track_genre"] :
            print("invalid feature..\n")
            return
        t2 = []
        for r in track_list :
            i = getattr(r , feature_name)
            try :
                t2.append(float(i))
            except (ValueError , TypeError) :
                 continue
        np_arr = np.array(t2)
        mean_val = np.mean(np_arr)
        std_val = np.std(np_arr)
        low = mean_val (- 3 * std_val)
        up = mean_val + (3 * std_val)
        for r in track_list :
            try :
                i = getattr(r , feature_name)
                if float(i) > up :
                    setattr(r,feature_name,up)
                    outlier_report.append(f"track : {track_list.index(r) + 1} . has outlier value : {i} and we fixed it with zcoreoutlierhandler . after fixing : {up} . ")
                elif low > float(i) :
                    setattr(r,feature_name,low)
                    outlier_report.append(f"track : {track_list.index(r) + 1} . has outlier value : {i} and we fixed it with zscoreoutlierhandler . after fixing : {low} . ")
            except (ValueError , TypeError) :
                 continue
            
            

