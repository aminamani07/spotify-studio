import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

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
        box = plt.boxplot(t2 , patch_artist=True)
        if "before" in title.lower():
            b_color = '#ff9999'
        else :
            b_color = '#99ff99'
        for p in box['boxes']:
            p.set_facecolor(b_color)
            p.set_edgecolor('#333333')
        for m in box['medians']:
            m.set_color('#111111')
            m.set_linewidth(2)
        plt.title(t)
        plt.ylabel(feature_name)
        plt.xlabel("Data Distribution")
        plt.show()
    def scatterplot(self, feature_x, feature_y):
        tx = []
        ty = []
        genres = []
        for r in self.track_list:
            i = getattr(r, feature_x)
            j = getattr(r, feature_y)
            g = getattr(r, "track_genre")
            tx.append(float(i))
            ty.append(float(j))
            genres.append(g)
        top_genres = [genre for genre, count in Counter(genres).most_common(10)]
        filtered_tx = []
        filtered_ty = []
        filtered_genres = []
        for x, y, g in zip(tx, ty, genres):
            if g in top_genres:
                filtered_tx.append(x)
                filtered_ty.append(y)
                filtered_genres.append(g)
        u_genres = top_genres
        color_ind = [u_genres.index(g) for g in filtered_genres]
        t = "Scatter plot ; " + feature_x + " vs " + feature_y
        plt.clf()
        scatter = plt.scatter(filtered_tx,filtered_ty,c=color_ind,cmap='viridis',alpha=0.7,s=3)
        plt.title(t)
        plt.xlabel(feature_x)
        plt.ylabel(feature_y)
        plt.legend(handles=scatter.legend_elements()[0],labels=u_genres,title="Genres")
        plt.setp(plt.gca().get_legend(),bbox_to_anchor=(1.05, 1))
        plt.tight_layout()
        plt.show()
    def plot_correlation_matrix(self , features):
        n = len(features)
        data = {}
        for f in features :
            data[f] = [float(getattr(r , f)) for r in self.track_list]
        matrix = [[0.0] * n for ii in range(n)]
        for i in range(n):
            for j in range(n):
                try :
                    X = data[features[i]]
                    Y = data[features[j]]
                    meanx = sum(X)/len(X)
                    meany = sum(Y)/len(Y)
                    num = sum((x - meanx) * (y - meany) for x,y in zip(X , Y))
                    denx = sum((x - meanx) ** 2 for x in X)
                    deny = sum((y - meany) ** 2 for y in Y)
                    if denx == 0 or deny == 0 :
                        matrix[i][j] = 0
                    else :
                        matrix[i][j] = num / ((denx * deny)** 0.5)
                except Exception :
                    matrix[i][j]= 0
        plt.clf()
        fig, ax = plt.subplots(figsize=(8, 6))
        
        im = ax.imshow(matrix, cmap='bwr', vmin=-1, vmax=1)
        
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel("Correlation Coefficient", rotation=-90, va="bottom")
        
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.set_xticklabels(features, rotation=45, ha="right")
        ax.set_yticklabels(features)
        
        for col in range(n):
            for row in range(n):
                text_color = "black" if abs(matrix[col][row]) < 0.7 else "white"
                ax.text(row, col , f"{matrix[col][row]:.2f}", 
                        ha="center", va="center", color=text_color, fontweight='bold')
        
        plt.title("Audio Features Correlation Matrix", pad=20)
        plt.tight_layout()
        fig.show()
    def plot_wordcloud(self , feature_name):
        txt = " ".join([getattr(r , feature_name , "") for r in self.track_list])
        wc = WordCloud(width=800 , height=400,background_color='white').generate(txt)
        plt.clf()
        plt.title(f"Wordcloud : {feature_name}")
        plt.imshow(wc , interpolation='bilinear')
        plt.axis("off")
        plt.show()


