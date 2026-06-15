import os
import pygame
import random
from src.song import Song
from src.data_loader import Data_loader
from src.data_analyzer import Dataanalyzer
from src.data_visualizer import Datavisualizer
from src.data_cleaner import MeanImputer , MedianImputer , KNNImputer , BaseImputer , BaseOutlierHandler , ZScoreOutlierHandler , IQROutlierHandler


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    features = ["track_id" , "artists", "album_name" , "track_name", "popularity", "duration_ms",
"explicit" , "danceability" , "energy", "key", "loudness", "mode", "speechiness",
"acousticness", "instrumentalness", "liveness", "valence", "tempo", "time_signature",
"track_genre"]
    f_path = "data/dataset.csv"
    if not os.path.exists(f_path):
        print(f"file {f_path} doesn't exist")
        return 
    else :
        print("loading... pleas wait...")
        loader = Data_loader(f_path)
        loader.read_data()
        print(f"load sucsessfull ... we can load {len(loader.track_list)} track from your file . ")
        print("================================\n*** WELCOM TO SPOTIFY STUDIO ***\n=====================================\n")
        pygame.mixer.init()
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(-1) #repeat when it music time finish
        while(True):
            try :
                print("pleas choose one of these items : \n1 . handle missing values (imputation)\n2 . handle outliers (clipping)\n3 . display statistical summary\n4 . data stroytelling & visualization\n5 . add a new track to dataset\n6 . reset dataset (reload original data)\n7 . save & exit")
                n = int(input("\nyour choice (1 - 7) : ").strip())
                print("-" * 40)
            except ValueError as e :
                print(e)
                n = 9
            if n == 7 :
                loader.save_data()
                st = input("do you want to exit ? (y/n) : ")
                if st in ["y","yes","Y"]:
                    print("goodbye dear ... nice to see you . ")
                    pygame.mixer.music.stop()
                    break
            elif n == 1 :
                while(True) :
                    try :
                        print("pleas choose one of this items that you want : \n1 . fulling missing values with using Mean (one feature) \n2 . fulling missing values with using Median (one feature) \n3 . fulling missing values with using LNN or machine learing (all features)")
                        ch = int(input("pleas enter your choice (1 - 3) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 5
                    if ch == 1 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            imputer = MeanImputer()
                            imputer.impute(loader.track_list , fe.lower())
                            print(f"missing values in {fe} replaced using Mean")
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 2 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            imputer = MedianImputer()
                            imputer.impute(loader.track_list , fe.lower())
                            print(f"missing values in {fe} replaced using Median")
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 3 :
                        imputer = KNNImputer()
                        imputer.impute(loader.track_list)
                        print(f"missing values replaced using KNN and machine learing")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    else :
                        print("invalid choice ... pleas try again . ")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
            elif n == 2 :
                while(True) :
                    try :
                        print("pleas choose one of this items that you want : \n1 . handling outlier values with using IQROutlier (one feature) \n2 . handling outlier values with using ZScoreOutlier (one feature) ")
                        ch = int(input("pleas enter your choice (1 - 2) : ").strip())
                    except ValueError as e :
                        ch = 3
                        print(e)
                    if ch == 1 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            handle = IQROutlierHandler()
                            handle.handle(loader.track_list , fe.lower())
                            print(f"outlier values in {fe} handled IQROutlier ")
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 2 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            handle = ZScoreOutlierHandler()
                            handle.handle(loader.track_list , fe.lower())
                            print(f"outlier values in {fe} handled ZScoreOutlier ")
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    else :
                        print("invalid choice ... pleas try again . ")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
            elif n == 3 :
                analyzer = Dataanalyzer(loader.track_list)
                while(True) :
                    try :
                        print("pleas choose one of this items : \n1 . Mean (one feature) \n2 . Median (one feature) \n3 . Maximum (one feature) \n4 . Minimum (one feature) \n5 . Varians (one feature) \n6 . Standard_Divation (one feature) \n7 . Mode (one feature) \n8 . Filter by artist \n9 . Filter by genre \n10 . Get top tracks (in one feature) \n11 . Recommend (in one feature) ")
                        ch = int(input("pleas enter your choice (1 - 11) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 14
                    if ch == 1 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_mean(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 2 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_median(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 3 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_maximum(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 4 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_minimum(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 5 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_varians(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 6 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_standarad_deviation(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 7 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            print(analyzer.analyze_mode(fe.lower()))
                        else :
                            print("invalid feature !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 8 :
                        artist = input("enter your artist : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        l = analyzer.filter_by_artist(artist , m)
                        if not l :
                            print("No tracks found !")
                        else :
                            print("______results______")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 9 :
                        genre = input("enter your genre : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        l = analyzer.filter_by_genre(genre , m)
                        if not l :
                            print("No tracks found !")
                        else :
                            print("______results______")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 10 :
                        fe = input("enter your feature : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        l = analyzer.get_top_tracks(fe , m)
                        if not l :
                            print("No tracks found !")
                        else :
                            print("______results______")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 11 :
                        fe = input("enter your feature : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        t_name = input("enter your track name : ").strip()
                        l = []
                        for r in loader.track_list :
                            if getattr(r , "track_name") == t_name :
                                l = analyzer.recommend(fe , m , r)
                                break
                        if l :
                            print("______results______")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                        else :
                            print("No tracks found !")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    else :
                        print("invalid choice ... pleas try again . ")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
            elif n == 4 :
                datavisualizer = Datavisualizer(loader.track_list)
                while(True) :
                    try :
                        print("pleas choose one of this items that you want : \n1 . Box plot designing (one feature) \n2 . Scatter plot designing (for two feature) \n3 . Correlation matrix designing or Heatmap (all features)\n4 . Wordcloud plot (one feature (str))")
                        ch = int(input("pleas enter your choice (1 - 4) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 5
                    if ch == 1 :
                        title = input("pleas enter your the title (before / after __ cleaning dataset by using '{}' )" ).strip()
                        fe = input("enter your feature : ").strip().lower()
                        if fe.lower() in features :
                            datavisualizer.boxplot(title , fe.lower())
                        else :
                            print("invalid feature !")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 3 :
                        fe = []
                        m = int(input("enter the features that you want to design a correlation matrix for them : "))
                        c = 0
                        while(c < m):
                            f = input(f"* feature {c+1} : ")
                            if f.lower() in features :
                                fe.append(f.lower())
                                c += 1
                            else :
                                print("invalid feature ! ")
                        datavisualizer.plot_correlation_matrix(fe)
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 2 :
                        r_list = random.sample(loader.track_list , 1000)
                        data_v = Datavisualizer(r_list)
                        f1 = input("enter first feature : ").strip()
                        f2 = input("enter second feature : ").strip()
                        if f1.lower() in features and f2.lower() in features :
                            data_v.scatterplot(f1.lower() , f2.lower())
                        else :
                            print("invalid features ! ")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 4 :
                        fe = input("enter your feature : ").strip().lower()
                        if fe.lower() in features :
                            datavisualizer.plot_wordcloud(fe.lower())
                        else :
                            print("invalid feature name !!!")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    else :
                        print("invalid choice ... pleas try again . ")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
            elif n == 5 :
                try :
                    print("okkk , now its time the enter your your track variables (20 variable) ... one by one . ")
                    track_id = input("enter your track id : ").strip()
                    artists = input("enter your track artist : ").strip()
                    album_name = input("enter your track album_name : ").strip()
                    track_name = input("enter your track name : ").strip()
                    popularity = input("enter your track popularity : ").strip()
                    duration_ms = input("enter your track duration_ms : ").strip()
                    explicit = input("enter your track explicit : ").strip()
                    danceability = input("enter your track danceability : ").strip()
                    energy = input("enter your track energy : ").strip()
                    key = input("enter your track key : ").strip()
                    loudness = input("enter your track loudness : ").strip()
                    mode = input("enter your track mode : ").strip()
                    speechiness = input("enter your track speechiness : ").strip()
                    acousticness = input("enter your track acousticness : ").strip()
                    instrumentalness = input("enter your track instrumentalness : ").strip()
                    liveness = input("enter your track liveness : ").strip()
                    valence = input("enter your track valence : ").strip()
                    tempo = input("enter your track tempo : ").strip()
                    time_signature = input("enter your track time_signature : ").strip()
                    track_genre = input("enter your track track_genre : ").strip()
                    new_song = Song(track_id, artists, album_name, track_name, popularity, duration_ms,
    explicit, danceability, energy, key, loudness, mode, speechiness,
    acousticness, instrumentalness, liveness, valence, tempo, time_signature,
    track_genre)
                    loader.append_track(new_song)
                    sa = input("do you want to save changes in last output file ? (y/n) : ")
                    if sa in ["y","yes","Yes"]: 
                        loader.save_data()
                except ValueError as e :
                    print(e)
            elif n == 6 :
                loader.reset_data()
            else :
                print("invalid number ... pleas try again ... ")



if __name__ == "__main__" :
    
    main()