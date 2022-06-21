"""  kNN Demo """
# 2 Klassenproblem -> Brustkrebs Ja/Nein?
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Laden des integrierten Datensatzes
cancer = load_breast_cancer()

# Starre Aufteilung in Trainings und Testmenge
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target,
                                                    random_state=42)
# train_test_split: 1 Parameter: Datensatz | 2P: Zielvariable (X und Y) Merkmale und Zielvariable | 3P: stratify -> Möchte schauen, dass die
# Klassenzugehörigkeit gleich verteilt wird. Somit wird die Zielvariable aus dem Datensatz gleich verteilt
# auf Training- und Testmenge. | 4P: random_state -> Mache das ganze reproduzierbar (Selbes Ergebnis beim
# nächsten Start des Programms -> wird gleiche Aufteilugn der Daten machen (wenn man irgendeine Zahl zuweist))
# X_train -> Trainingsmenge
# X_test -> Testmenge
# y_train -> Zielvariable Trainingsmenge
# y_test -> Zielvariable Testmenge


# Standard k-NN classsification
knn = KNeighborsClassifier(n_neighbors=1)
# n_neighbors=.. -> Anzahl nächster Nachbarn


# Bis 05:11 gesehen