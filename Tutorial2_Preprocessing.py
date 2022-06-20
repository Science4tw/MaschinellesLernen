###############################################################################
""" Tutorial 2 - Daten laden, Vorverarbeiten und Visualisieren """

# 2.1.1 Eigene Synthetische Daten Erzeugen
""" Das Modul sklearn.datasets enth¨alt Funktionen, die synthetische Datenmengen
erzeugen. Mit der Funktion make_classification k¨onnen wir einen synthetischen
Datensatz mit beliebiger Anzahl Datenobjekte (n_samples), Merkmale (n_features)
und Klassen n_classes generieren lassen (n_redudandant gibt an, wie viele der
Merkmale redundant sein sollen – es existieren weitere solche Parameter). Die Ruckgabe ¨
der Funktion sind die Merkmale X und die Zielvariable y. """

import sklearn.datasets as ds
import matplotlib.pyplot as plt
# creates an own toy example with 100 data objects described by
# two features stemming from two classes
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)
# printing out both the features and the target
print(X)    # Die Ausgabe von print(X) ist bspw.: [[ 1.96993256 -0.96326783] ..... [ 1.09754161 1.51609973]]
print(y)    # Und die Ausgabe von print(y) ist bspw.: [1 0 1 0 0 0 1 1 0 ... 0 1 1 1]

# plotting the dataset with a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Data Set with 100 Data Objects, 2 Features, 2 Classes')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()

""" Es sieht also so aus, als ob X und y Listen sind – tats¨achlich sind dies aber sogenannte
NumPy Arrays. W¨ahrend eine Python-Liste verschiedene Datentypen innerhalb einer
einzigen Liste enthalten kann, sollten alle Elemente in einem NumPy Array vom gleichen Typ sein.
NumPy Arrays sind schneller und verbrauchen weniger Speicher als Python-Listen."""

""" Glucklicherweise verhalten sich ¨ NumPy Arrays fast gleich wie Listen. Zum Beispiel
funktioniert der Zugriff auf einzelne Elemente via Index oder Slicing genau gleich
wie bei Listen: """
import numpy as np
# one-dimensional array
a = np.array([1, 2, 3, 4, 5, 6])
print(a[3]) # 4
print(a[2:5]) # [3 4 5]

# two-dimensional array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0]) # [1 2 3 4]
print(a[2][3]) # 12

""" Zus¨atzlich bieten NumPy Arrays ein paar Attribute an, welche einige Merkmale der
Daten speichern (Anzahl Dimensionen, Anzahl Elemente Total, Anzahl Elemente
pro Dimension): """
# functions on an array
print(a.ndim) # number of dimensions = 2
print(a.size) # number of elements = 12
print(a.shape) # size of data (rows, cols) = (3, 4)

""" Der grösste Unterschied zu Listen bzgl. der Syntax ist der Zugriff auf ganze Zeilen
oder Spalten:"""
# complete or parts of rows from the array
row1 = a[1, :] # equivalent to: row1 = a[1]
print(row1) # [5 6 7 8]
part_of_row1 = a[1, 1:3]
print(part_of_row1) # [6 7]

# complete columns from the array (not possible on lists!)
col0 = a[:, 0]
print(col0) # [1 5 9]

""" Eine der besten M¨oglichkeiten, Daten zu untersuchen, ist, diese zu visualisieren. Eine Möglichkeit,
 dies zu tun, ist die Verwendung eines Streudiagramms. In obigem
Beispiel verwenden wir hierzu das Modul matplotlib.pyplot und die Funktion
scatter: Auf der x-Achse befinden sich die Werte der 0. Spalte (X[:, 0]) und auf
der y-Achse die Werte der 1. Spalte der Datenobjekte (X[:, 1]). Jedes Datenobjekt wird nun in der Ebene gemäss seinen
 Merkmalen als Punkt gezeichnet – die Farbe c des Punktes ist durch die Klasse der jeweiligen Datenobjekte gegeben
(siehe Abb. 2.1). """

# 2.1.2 Integrierte Standard-Daten
""" Das Projekt scikit-learn wird mit ein paar kleinen, realen Standard-Datens¨atzen
geliefert, fur die Sie keine externe Datei laden m ¨ ussen. Jeder dieser Datensätze kann Abbildung 2.1: Visualisieren eines synthetischen Datensatzes mit Datenobjekten, die aus
zwei Klassen stammen und mit zwei Merkmalen beschrieben sind.
mit einer eigenen Funktion aus dem Modul datasets geladen werden (z.B. load_iris()
oder load_breast_cancer()).
Die Ruckgabe dieser Funktionen ist ein sogenanntes ¨ Bunch. Ein Bunch verh¨alt sich
¨ahnlich wie ein W¨orterbuch dict, das alle Daten und einige Metadaten uber die ¨
Daten enth¨alt. Die Merkmalswerte der Daten werden im Element mit Schlussel ¨
"data" gespeichert, das ein zweidimensionales NumPy Array der Gr¨osse N × n ist
(Anzahl Datenobjekte × Anzahl Merkmale). Die Namen der Merkmale kann man
in der Liste mit Schlussel ¨ "feature_names" finden und im Falle eines uberwachten ¨
Problems wird im Array mit dem Schlussel ¨ "target" die Zielvariable gespeichert. """

from sklearn import datasets
# load an integrated dataset
iris = datasets.load_iris()
# key data gives access to the features
print(iris["data"])
# key target gives the ground truth for the iris dataset
print(iris["target"])
# key feature_names gives a list of the feature names
print(iris["feature_names"])

""" Die Ausgabe des obigen Programmes lautet:
[[5.1 3.5 1.4 0.2]
[4.9 3. 1.4 0.2]
[4.7 3.2 1.3 0.2]
...
[5.9 3. 5.1 1.8]]
[0 0 0 0... 2 2 2]
[’sepal length (cm)’, ’sepal width (cm)’, ’petal length (cm)’, ’petal width
(cm)’]
"""

""" Hinweis: In einem Bunch ist es im Gegensatz zu einem W¨orterbuch m¨oglich, die Werte eines Schlussels statt mit ¨ iris["data"] auch direkt mit iris.data auszulesen.
Wir werden zwischendurch die Datenstruktur DataFrame des externen Paketes pandas
verwenden. Ein DataFrame kann man sich wie eine Tabellenblatt in Excel vorstellen: Jede Zeile (d.h. jedes Datenobjekt) ist nummeriert (0, 1, 2, . . .) und jede Spalte (d.h. jedes Merkmal) wird mit dem Namen des Merkmales beschriftet.
Um ein DataFrame zu erzeugen ben¨otigen wir also die Merkmale der Datenobjekte
(iris["data") und die Namen der Merkmale (iris["feature_names"):"""
from sklearn import datasets
import pandas as pd
# load an integrated dataset
iris = datasets.load_iris()
# create dataframe from data in iris.data
# label the columns using the strings in iris.feature_names
X, f = iris["data"], iris["feature_names"]
iris_dataframe = pd.DataFrame(X, columns=f)
print(iris_dataframe)