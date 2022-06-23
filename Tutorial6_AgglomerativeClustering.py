""" Demo Clustering """
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

""" Hierarchisches Verfahren Beispiel 1 (Start)"""
# Funktion make_blobs() -> Erzeugt mir im 2-D Raum Datenhaufen
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)
plt.scatter(X[:, 0],
            X[:, 1])
# 1P: Alles aus der 0-ten Spalte von X (Erstes Element von X bis...
# 2P:Alles aus der 1-ten Spalte von X
plt.xlabel("Merkmal 1")
plt.ylabel("merkmal 2")
plt.show()
# Bei einer Echt-Welt-Anwendung hätten wir logischerweise keine Ahnung wie viele Zentren etc. wir hätten

# Möglichkeit für Clustering:
agg_clustering = AgglomerativeClustering(linkage="complete", n_clusters=4)
# Linkage -> z.b. single oder complete (gibt auch weitere)
# n_clusters -> Anzahl Cluster (Nehmen 4, da wirs schon wissen vom toy-example)

assignment = agg_clustering.fit_predict(X) # Assignment (Cluster-Zugehörigkeit) definieren bzw. trainieren&vorhersagen
plt.scatter(X[:, 0], X[:, 1], c=assignment) # c -> Farbe -> Nach Cluster Zugehörigkeit
plt.show()
print(assignment) # Ausgabe der Cluster-Zugehörigkeit

# Typischerweise, haben wir das Problem, dass wir die optimale Anzahl an Clustern nicht kennen
# Aufgabe: find optimal number of Clusters -> Mit indices wie z.B. Silhouette Index
# For in range Schleife für 2-9 Cluster
for k in range(2, 10):
    # testen mit complete Linkage
    agg_complete = AgglomerativeClustering(linkage="complete", n_clusters=k)
    assignment_complete = agg_complete.fit_predict(X)

    # testen mit single Linkage
    agg_single = AgglomerativeClustering(linkage="single", n_clusters=k)
    assignment_single = agg_single.fit_predict(X)

    # Silhouette score braucht: Daten X und die Cluster-Zugehörigkeit (assignment)
    # Je grösser der Silhouette Wert desto besser
    score_complete = silhouette_score(X, assignment_complete)
    print("(Complete-Linkage) -> Kluster (k) =", k, "Silhouette-Index score=", score_complete)
    # -> Mit complete-linkage und Silhouette-Index wäre die optimale Anzahl Klsuter bei k=4 mit einem score von ca 0.8

    score_single = silhouette_score(X, assignment_single)
    # print("(Single-Linkage) -> Kluster (k) =", k, "Silhouette-Index score=", score_single)


""" Hierarchisches Verfahren Beispiel 1 (Ende)"""

