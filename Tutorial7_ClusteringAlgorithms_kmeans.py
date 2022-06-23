""" k-means """
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)

kmeans = KMeans(n_clusters=4, n_init=100)
# n_init -> Wieviel mal der Algo gestartet wird und sucht das beste Clustering bezüglich der minimalen Fehler E tief k
kmeans.fit(X) # Nur auf X ist ja Unüberwachtes Lernen

print("Clusterzugehörigkeiten: ", kmeans.labels_)
print("Zentroide: ", kmeans.cluster_centers_) # Haben ja nur 2 Merkmale, deshalb auch 2D Zentroide | -> Koodinaten
plt.scatter(X[:, 0],X[:, 1], c= kmeans.labels_) # Alle Zeilen aus der 0-ten Spalte, 1-ten Spalte, mit der
# Farbe der Labels
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c="black") #Markiert Zentren der Cl. schwarz
plt.xlabel("Merkmale  1")
plt.ylabel("Merkmale 2")
plt.show()

