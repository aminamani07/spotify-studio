import os
from src.song import Song
from src.data_loader import Data_loader
from src.data_analyzer import Dataanalyzer
from src.data_visualizer import Datavisualizer
from src.data_cleaner import MeanImputer , MedianImputer , KNNImputer , BaseImputer , BaseOutlierHandler , ZScoreOutlierHandler , IQROutlierHandler

def main():
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
            n = int(input("\nyour choice (1 - 6) : ").strip())
            print("-" * 40)
            if n == 7 :
                #save#
                print("goodbye dear ... nice to see you . ")
                break
            elif n == 1 :
                pass
            elif n == 2 :
                pass
            elif n == 3 :
                pass
            elif n == 4 :
                pass
            elif n == 5 :
                pass
            elif n == 6 :
                pass
            else :
                print("invalid number ... pleas try again ... ")



if __name__ == "__main__" :
    main()