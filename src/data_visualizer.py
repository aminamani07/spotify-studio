import matplotlib.pyplot as plt

class Datavisualizer :
    def __init__(self , track_list):
        self.track_list = track_list
    def boxplot(self , title , feature_name):
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        t = feature_name.upper() + " : " + title
        plt.clf()
        plt.boxplot(t2)
        plt.title(t)
        plt.ylabel(feature_name)
        plt.xlabel("Data Distribution")
        plt.show()
        
