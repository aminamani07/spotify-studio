import os
import pygame
import random
from src.data_loader import s3s
from src.song import Song
from src.data_loader import Data_loader
from src.data_analyzer import Dataanalyzer
from src.data_visualizer import Datavisualizer
from src.data_cleaner import missing_report , outlier_report
from src.data_cleaner import MeanImputer , MedianImputer , KNNImputer , BaseImputer , BaseOutlierHandler , ZScoreOutlierHandler , IQROutlierHandler


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


features = ["track_id" , "artists", "album_name" , "track_name", "popularity", "duration_ms",
"explicit" , "danceability" , "energy", "key", "loudness", "mode", "speechiness",
"acousticness", "instrumentalness", "liveness", "valence", "tempo", "time_signature",
"track_genre"]

fet2 = ["explicit", "track_id" , "track_name" , "artists" , "album_name" , "track_genre"]

def feature_menu():
    for ind , fe in enumerate(features) :
        print(f"{ind + 1} . {fe}")
    print("\n")
    inte = int(input("enter your choice (1 - 20) : ").strip())
    print("\n")
    if 1 <= inte <= 20 :
        return features[inte - 1]
    else :
        return "none"

def main():
    f_path = "data/dataset.csv"
    if not os.path.exists(f_path):
        print(f"file {f_path} doesn't exist\n")
        return 
    else :
        pygame.mixer.init()
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(-1) #repeat when it music time finish
        print("loading... pleas wait...\n")
        loader = Data_loader(f_path)
        loader.read_data()
        print(f"load sucsessfull ... we could load {len(loader.track_list)} track from your file . \n")
        print("==================================\n*** WELCOM TO SPOTIFY STUDIO ***\n=====================================\n")
        print(f"at first i want to say that in some tracks we have missing string values and we remove them from out data . and the id (number) of them in first dataset : {s3s} ... keep going.")
        input("press enter to continue ...")
        while(True):
            clear_terminal()
            try :
                print("pleas choose one of these items : \n1 . handle missing values (imputation)\n2 . handle outliers (clipping)\n3 . display statistical summary\n4 . data stroytelling & visualization\n5 . add a new track to dataset\n6 . reset dataset (reload original data)\n7 . missing values report\n8 . outlier values report\n9 . save \n10 . exit \n")
                n = int(input("\nyour choice (1 - 8) : ").strip())
                print("-" * 40)
            except ValueError as e :
                print(e)
                n = 9
            if n == 9 :
                loader.save_data()
                st = input("do you want to exit ? (y/n) : ")
                if st in ["y","yes","Y"]:
                    clear_terminal()
                    print("goodbye dear ... nice to see you . \n")
                    pygame.mixer.music.stop()
                    break
            elif n == 10 :
                clear_terminal()
                print("goodbye dear ... nice to see you . \n")
                pygame.mixer.music.stop()
                break
            elif n == 1 :
                while(True) :
                    clear_terminal()
                    try :
                        print("pleas choose one of this items that you want : \n1 . fulling missing values with using Mean (one feature... number features) \n2 . fulling missing values with using Median (one feature... number features) \n3 . fulling missing values with using KNN or machine learing (all features)\n")
                        ch = int(input("pleas enter your choice (1 - 3) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 5
                    if ch == 1 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() not in fet2 :
                            imputer = MeanImputer()
                            imputer.impute(loader.track_list , fe.lower())
                            print(f"missing values in {fe} replaced using Mean\n")
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            break
                    elif ch == 2 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() not in fet2 :
                            imputer = MedianImputer()
                            imputer.impute(loader.track_list , fe.lower())
                            print(f"missing values in {fe} replaced using Median\n")
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 3 :
                        imputer = KNNImputer()
                        imputer.impute(loader.track_list)
                        print(f"missing values replaced using KNN and machine learing\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    else :
                        print("invalid choice ... pleas try again . \n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
            elif n == 2 :
                while(True) :
                    clear_terminal()
                    try :
                        print("pleas choose one of this items that you want : \n1 . handling outlier values with using IQROutlier (one feature ... number features) \n2 . handling outlier values with using ZScoreOutlier (one feature... number features) \n")
                        ch = int(input("pleas enter your choice (1 - 2) : ").strip())
                    except ValueError as e :
                        ch = 3
                        print(e)
                    if ch == 1 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() not in fet2 :
                            handle = IQROutlierHandler()
                            handle.handle(loader.track_list , fe.lower())
                            print(f"outlier values in {fe} handled IQROutlier \n")
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 2 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() not in fet2 :
                            handle = ZScoreOutlierHandler()
                            handle.handle(loader.track_list , fe.lower())
                            print(f"outlier values in {fe} handled ZScoreOutlier \n")
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    else :
                        print("invalid choice ... pleas try again . \n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
            elif n == 3 :
                analyzer = Dataanalyzer(loader.track_list)
                while(True) :
                    clear_terminal()
                    try :
                        print("pleas choose one of this items : \n1 . Mean (one feature... number features) \n2 . Median (one feature... number features) \n3 . Maximum (one feature... number features) \n4 . Minimum (one feature... number features) \n5 . Varians (one feature... number features) \n6 . Standard_Divation (one feature... number features) \n7 . Mode (one feature... number features) \n8 . Filter by artist \n9 . Filter by genre \n10 . Get top tracks (in one feature... number features) \n11 . Recommend (in one feature... number features) \n")
                        ch = int(input("pleas enter your choice (1 - 11) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 14
                    if ch == 1 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_mean(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 2 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_median(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 3 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_maximum(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 4 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_minimum(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 5 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_varians(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 6 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_standarad_deviation(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 7 :
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            print(analyzer.analyze_mode(fe.lower()))
                        else :
                            print("invalid feature !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 8 :
                        artist = input("enter your artist : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        clear_terminal()
                        l = analyzer.filter_by_artist(artist , m)
                        if not l :
                            print("No tracks found !\n")
                        else :
                            print("___________________________RESULTS_____________________________")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                            print()
                        ex = input("\ndo you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 9 :
                        genre = input("enter your genre : ").strip().lower()
                        m = int(input("enter the number of tracks you want : ").strip())
                        clear_terminal()
                        l = analyzer.filter_by_genre(genre , m)
                        if not l :
                            print("No tracks found !\n")
                        else :
                            print("________________________RESULTS____________________________")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                            print()
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 10 :
                        fe = feature_menu()
                        m = int(input("enter the number of tracks you want : ").strip())
                        clear_terminal()
                        l = analyzer.get_top_tracks(fe , m)
                        if not l :
                            print("No tracks found !\n")
                        else :
                            print("_____________________________RESULTS________________________________")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                            print()
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 11 :
                        fe = feature_menu()
                        m = int(input("enter the number of tracks you want : ").strip())
                        t_name = input("enter your track name : ").strip()
                        clear_terminal()
                        l = []
                        for r in loader.track_list :
                            if getattr(r , "track_name") == t_name :
                                l = analyzer.recommend(fe , m , r)
                                break
                        if l :
                            print("____________________________RESULTS_____________________________")
                            for id , song in enumerate(l , 1):
                                print(f"{id} . {song.track_name} by {song.artists} . ( Genre : {song.track_genre} )")
                            print()
                        else :
                            print("No tracks found !\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    else :
                        print("invalid choice ... pleas try again . \n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
            elif n == 4 :
                datavisualizer = Datavisualizer(loader.track_list)
                while(True) :
                    clear_terminal()
                    try :
                        print("pleas choose one of this items that you want : \n1 . Box plot designing (one number feature) \n2 . Scatter plot designing (for two number features) \n3 . Correlation matrix designing or Heatmap (all number features)\n4 . Wordcloud plot (one feature (str))\n")
                        ch = int(input("pleas enter your choice (1 - 4) : ").strip())
                    except ValueError as e :
                        print(e)
                        ch = 5
                    if ch == 1 :
                        title = input("pleas enter your the title (before / after __ cleaning dataset by using '{}' ) : " ).strip()
                        fe = feature_menu()
                        clear_terminal()
                        if fe.lower() in features :
                            datavisualizer.boxplot(title , fe.lower())
                        else :
                            print("invalid feature !\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 3 :
                        fe = []
                        m = int(input("enter the number of features that you want to design a correlation matrix for them : "))
                        c = 0
                        while(c < m):
                            print(f"feature {c + 1}")
                            f = feature_menu()
                            clear_terminal()
                            if f.lower() in features :
                                fe.append(f.lower())
                                c += 1
                            else :
                                print("invalid feature ! \n")
                        datavisualizer.plot_correlation_matrix(fe)
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 2 :
                        #r_list = random.sample(loader.track_list , 1000)
                        #data_v = Datavisualizer(r_list)
                        print("first feature : ")
                        f1 = feature_menu()
                        clear_terminal()
                        print("second feature : ")
                        f2 = feature_menu()
                        clear_terminal()
                        if f1.lower() in features and f2.lower() in features :
                            datavisualizer.scatterplot(f1.lower() , f2.lower())
                        else :
                            print("invalid features ! \n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    elif ch == 4 :
                        di = {"1" : "artists" , "2" : "album_name" , "3" : "track_genre" , "4" : "track_name"}
                        fee = input("\npleas choose your feature : \n1 . artists\n2 . album_name\n3 . track_genre\n4 . track_name\nyour choice number : ").strip()
                        if fee in list(di.keys()):
                            fe = di[fee]
                        else :
                            fe = None
                        clear_terminal()
                        if fe.lower() in features :
                            datavisualizer.plot_wordcloud(fe.lower())
                        else :
                            print("invalid feature name !!!\n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
                    else :
                        print("invalid choice ... pleas try again . \n")
                        ex = input("do you want to exit this part and go back ? (y/n) : ").strip()
                        if ex in ["y","yes","Yes"]:
                            clear_terminal()
                            break
            elif n == 5 :
                while True :
                    clear_terminal()
                    try :
                        print("okkk , now its time the enter your your track variables (20 variable) ... one by one . \n")
                        id = len(loader.track_list) + 1
                        track_id = input("enter your track id : ")
                        if track_id == "" or track_id.strip() == "" :
                            print("Error : track id cannot be empty! going back to menu ...\n")
                            input("Press enter to continue...")
                            break
                        artists = input("enter your track artist : ")
                        if artists == "" or artists.strip() == "" :
                            print("Error : artists cannot be empty! going back to menu ...\n")
                            input("Press enter to continue...")
                            break
                        album_name = input("enter your track album_name : ")
                        if album_name == "" or album_name.strip() == "" :
                            print("Error : album name cannot be empty! going back to menu ...\n")
                            input("Press enter to continue...")
                            break
                        track_name = input("enter your track name : ")
                        if track_name == "" or track_name.strip() == "" :
                            print("Error : track name cannot be empty! going back to menu ...\n")
                            input("Press enter to continue...")
                            break
                        popularity = input("enter your track popularity (0 - 100) : ").strip()
                        duration_ms = input("enter your track duration_ms : ").strip()
                        explicit = input("enter your track explicit (1 , 0) ---> (1 : true , 0 : false) : ").strip()
                        danceability = input("enter your track danceability (0.0 - 1.0) : ").strip()
                        energy = input("enter your track energy (0.0 - 1.0) : ").strip()
                        key = input("enter your track key (0 - 11) : ").strip()
                        loudness = input("enter your track loudness (-60.0 - 0.0) : ").strip()
                        mode = input("enter your track mode (0 , 1) : ").strip()
                        speechiness = input("enter your track speechiness (0.0 - 1.0) : ").strip()
                        acousticness = input("enter your track acousticness (0.0 - 1.0) : ").strip()
                        instrumentalness = input("enter your track instrumentalness (0.0 - 1.0) : ").strip()
                        liveness = input("enter your track liveness (0.0 - 1.0) : ").strip()
                        valence = input("enter your track valence (0.0 - 1.0) : ").strip()
                        tempo = input("enter your track tempo (50 - 250) : ").strip()
                        time_signature = input("enter your track time_signature (milliseconds , > 0) : ").strip()
                        track_genre = input("enter your track track_genre : ")
                        if track_genre == "" or track_genre.strip() == "" :
                            print("Error : track genre cannot be empty! going back to menu ...\n")
                            input("Press enter to continue...")
                            break
                        new_song = Song(id , track_id, artists, album_name, track_name, popularity, duration_ms,
        explicit, danceability, energy, key, loudness, mode, speechiness,
        acousticness, instrumentalness, liveness, valence, tempo, time_signature,
        track_genre)
                        loader.append_track(new_song)
                        sa = input("do you want to save changes in last output file ? (y/n) : ")
                        if sa in ["y","yes","Yes"]: 
                            clear_terminal()
                            loader.save_data()
                        break
                    except (ValueError , Exception) as e :
                        print(e,"\n")
            elif n == 6 :
                clear_terminal()
                loader.reset_data()
            elif n == 7 :
                if missing_report :
                    try :
                        nu3 = int(input("the number of outlier handling data you want to see : ").strip())
                        if nu3 < len(outlier_report) :
                            x = nu3
                        else :
                            x = len(outlier_report)
                        print()
                        print("--------------------RESULTS-------------------")
                        for i , j in enumerate(missing_report[:x]):
                            print(f"{i + 1} . {j}")
                        print()
                        input("press enter to continue...")
                    except (ValueError , TypeError) :
                        continue
                else :
                    print("there isn't any report until now . ")
            elif n == 8 :
                if outlier_report :
                    try :
                        nu3 = int(input("the number of outlier handling data you want to see : ").strip())
                        if nu3 < len(outlier_report) :
                            x = nu3
                        else :
                            x = len(outlier_report)
                        print()
                        print("--------------------RESULTS-------------------")
                        for i , j in enumerate(outlier_report[:x]):
                            print(f"{i + 1} . {j}")
                        print()
                        input("press enter to continue...")
                    except (ValueError , TypeError) :
                        continue
                else :
                    print("there isn't any report until now . ")
            else :
                print("invalid number ... pleas try again ... \n")



if __name__ == "__main__" :
    clear_terminal()
    main()
    