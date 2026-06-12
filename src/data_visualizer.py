import matplotlib.pyplot as plt

class Datavisualizer :
    def __init__(self , track_list):
        self.track_list = track_list
    def popularity_boxplot(self , title , feature_name):
       