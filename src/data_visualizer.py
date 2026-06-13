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
        genres = []
        for r in self.track_list :
            i = getattr(r , feature_x)
            j = getattr(r , feature_y)
            g = getattr(r ,"genre")
            tx.append(float(i))
            ty.append(float(j))
            genres.append(g)
        u_genres = list(set(genres))
        color_ind = [u_genres.index(g) for g in genres]
        t = "Scatter plot ; " + feature_x + " vs " + feature_y
        plt.clf()
        plt.scatter(tx , ty , c=color_ind , cmap='viridis' , alpha=0.7)
        plt.title(t)
        plt.xlabel(feature_x)
        plt.ylabel(feature_y)
        plt.legend(handles=scatter.legend_elements()[0], labels=u_genres , title="Genres")
        plt.show()
    



