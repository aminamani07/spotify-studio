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





if __name__ == "__main__" :
    main()