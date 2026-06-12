import matplotlib.pyplot as plt

class Datavisualizer :
    def __init__(self , track_list):
        self.track_list = track_list
    def boxplot(self , title , feature_name):
        t2 = []
        for r in self.track_list :
            i = getattr(r , feature_name)
            t2.append(float(i))
        t = "Box plot ; " + feature_name.upper() + " : " + title
        plt.clf()
        plt.boxplot(t2)
        plt.title(t)
        plt.ylabel(feature_name)
        plt.xlabel("Data Distribution")
        plt.show()
    def scatterplot(self , feature_x , feature_y ):
        tx = []
        ty = []
        for r in self.track_list :
            i = getattr(r , feature_x)
            j = getattr(r , feature_y)
            tx.append(float(i))
            ty.append(float(j))
        t = "Scatter plot ; " + feature_x + " vs " + feature_y
        plt.clf()
        plt.scatter(tx , ty)
        plt.title(t)
        plt.xlabel(feature_x)
        plt.ylabel(feature_y)
        plt.show()



