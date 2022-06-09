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
