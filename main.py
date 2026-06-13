import os
from src.song import Song
from src.data_loader import Data_loader
from src.data_analyzer import Dataanalyzer
from src.data_visualizer import Datavisualizer
from src.data_cleaner import MeanImputer , MedianImputer , KNNImputer , BaseImputer , BaseOutlierHandler , ZScoreOutlierHandler , IQROutlierHandler

def main():
    features = []
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
        while(True):
            print("pleas choose one of these items : \n1 . handle missing values (imputation)\n2 . handle outliers (clipping)\n3 . display statistical summary\n4 . data stroytelling & visualization\n5 . add a new track to dataset\n6 . reset dataset (reload original data)\n7 . save & exit")
            n = int(input("\nyour choice (1 - 7) : ").strip())
            print("-" * 40)
            if n == 7 :
                loader.save_data()
                st = input("do you want to exit ? (y/n) : ")
                if st in ["y","yes","Y"]:
                    print("goodbye dear ... nice to see you . ")
                    break
            elif n == 1 :
                while(True) :
                    print("pleas choose one of this items that you want : \n1 . fulling missing values with using Mean (one feature) \n2 . fulling missing values with using Median (one feature) \n3 . fulling missing values with using LNN or machine learing (all features)")
                    ch = int(input("pleas enter your choice (1 - 3) : ").strip())
                    if ch == 1 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            imputer = MeanImputer()
                            imputer.impute(loader.track_list , fe)
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
                            imputer.impute(loader.track_list , fe)
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
            elif n == 2 :
                while(True) :
                    print("pleas choose one of this items that you want : \n1 . handling outlier values with using IQROutlier (one feature) \n2 . handling outlier values with using ZScoreOutlier (one feature) ")
                    ch = int(input("pleas enter your choice (1 - 3) : ").strip())
                    if ch == 1 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            handle = IQROutlierHandler()
                            handle.handle(loader.track_list , fe)
                            print(f"outlier values in {fe} handled IQROutlier ")
                        else :
                            print("invalid feature !!!")
                    elif ch == 2 :
                        fe = input("enter your feature : ").strip()
                        if fe.lower() in features :
                            handle = ZScoreOutlierHandler()
                            handle.handle(loader.track_list , fe)
                            print(f"outlier values in {fe} handled ZScoreOutlier ")
                        else :
                            print("invalid feature !!!")
                    else :
                        print("invalid choice ... pleas try again . ")
            elif n == 3 :
                pass
            elif n == 4 :
                pass
            elif n == 5 :
                pass
            elif n == 6 :
                loader.reset_data()
            else :
                print("invalid number ... pleas try again ... ")



if __name__ == "__main__" :
    main()