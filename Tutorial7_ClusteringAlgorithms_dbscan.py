""" dbscan """
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Künstlicher Datenhaufen mit 4 Klassen, 2 Merkmalen
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)

dbscan = DBSCAN(eps=1.2, min_samples=4)
# eps= .. -> Epsilon -> Radius
# min_samples=.. -> Teta -> Mindest Dichte
dbscan.fit(X)

print("Clusterzugehörigkeiten: ", dbscan.labels_)
plt.scatter(X[:, 0],X[:, 1], c= dbscan.labels_) # Alle Zeilen aus der 0-ten Spalte, 1-ten Spalte, mit der
# Farbe der Labels

plt.xlabel("Merkmale  1")
plt.ylabel("Merkmale 2")
plt.show()
