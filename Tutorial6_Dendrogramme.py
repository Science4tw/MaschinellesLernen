""" Hierarchisches Verfahren Beispiel 2 (Start)"""
# "Zeichnen" von Dendrogrammen

from sklearn.datasets import make_blobs
# mit scipy möglich Dendrogramme zu zeichnen
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import single, complete
import matplotlib.pyplot as plt

# Funktion make_blobs() -> Erzeugt mir im 2-D Raum Datenhaufen
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)
# Kann ein Linkage Array machen un kann die Funktion complete(Daten) oder single(Daten) aufrufen
linkage_array = complete(X)

# Dendrogramm erwartet das Linkage Array
dendrogram(linkage_array, color_threshold=15.0)
# color_threshold bedeutet, dass alles unter der Distanz von der Grenze liegt, kriegt eine andere Farbe
plt.xlabel("Datenobjekte")
plt.ylabel("Clusterdistanz")
plt.show()

""" Hierarchisches Verfahren Beispiel 2 (Ende)"""