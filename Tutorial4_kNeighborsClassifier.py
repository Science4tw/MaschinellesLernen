"""  kNN Demo """
# 2 Klassenproblem -> Brustkrebs Ja/Nein?
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Laden des integrierten Datensatzes
cancer = load_breast_cancer()

# Starre Aufteilung in Trainings und Testmenge
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target,
                                                    random_state=42)
# train_test_split: 1 Parameter: Datensatz | 2P: Zielvariable (X und Y) Merkmale und Zielvariable | 3P: stratify ->
# Möchte schauen, dass die
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

# Trainieren (wird jetzt eich. gar nichts gerlernt, die Traingsmenge ist das Modell selbst)
knn.fit(X_train, y_train)

# Vorhersage für jedes Testobjekt, jedes Testobjekt wird klassifiziert und in y_pred gesp.
y_pred = knn.predict(X_test)
print(y_pred) # Klassenzugehörigkeiten, welcher der kNN Klassifikator voraussagt

# Erkennungsrate auf der Testmenge mit den Test Klassenzugehörigkeiten
print("Test Score: ", knn.score(X_test, y_test))

# gewichtete kNN Klassifikation
knn = KNeighborsClassifier(n_neighbors=1, weights="distance") # Gewichtung mit der Distanz
knn.fit(X_train, y_train)
print("Test Score (weighted version): ", knn.score(X_test, y_test))

# Optimierung der Parameter (Also Anzahl Nachbarn um die Erkennungsrate zu erhöhen)
neighbors_setting = range(1,16,2) # Nachbarn (k) von 1 bis 15 in 2er Schritten
training_accuracy = [] # Leere Liste für Trainingsgenaugikeit
test_accuracy = [] # Leere Liste für Testgenaugikeit

# Trainiere ich den kNN Klassifikator für 1 bis 15 Nachbarn
for n in neighbors_setting:
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)

    # Füge die erhaltenen Test Erkennungsraten der Liste hinzu
    test_accuracy.append(knn.score(X_test, y_test))
    # Füge die erhaltenen Training Erkennungsraten der Liste hinzu
    training_accuracy.append(knn.score(X_train, y_train))

    # -> Teste meinen kNN mit k=1,k=2 etc. und überprüfe immer mit der Erkennungsrate wie gut es auf der Testmenge
    # und der Trainingsmenge funktioniert

# Anzeigen
plt.plot(neighbors_setting, training_accuracy, label="training accuracy")
# X Achse die Anzahl Nachbarn
# Y Achse die Trainings Erkennungsrate
plt.plot(neighbors_setting, test_accuracy, label="test accuracy (oder hier auch Validierungsmenge")
plt.xlabel("Erkennungsrate (Accuracy)")
plt.ylabel("Anzahl Nachbarn (number of neighbors)")
plt.legend() # Legende anzeigen
plt.show()


# Jetzt noch mit Kreuzvalidierung (Keine fixe Aufteilung in Trainings- & Testmenge)
from sklearn.model_selection import cross_val_score
X, y = cancer.data, cancer.target
knn = KNeighborsClassifier(n_neighbors=3)
scores = cross_val_score(knn, X, y, cv=5)
# 1P -> Das Model (kNN)
# 2P -> Daten
# 3P -> Zielvariable
# 4P -> cv=.. -> Anzahl Kreuzvalidierungen (folds)
print("Cross Validation Scores:", scores) # 5 Erkennungsraten auf den 5 folds mit 3 Nachbarn -->
# Cross Validation Scores: [0.87719298 0.92105263 0.94736842 0.93859649 0.91150442]
# Erster fold scheint schwieriger zu sein für die Klassifikation als die anderen
print("Cross Validation Scores Mean:", scores.mean()) # Gemittelt

# Automatisiertes testen, wieviele NAchbarn mit 10facher Kreuzvalidierung ideal sind (beste Erkennungsrate haben)
for n in neighbors_setting:
    knn = KNeighborsClassifier(n_neighbors=n)
    scores = cross_val_score(knn, X, y, cv=10)
    print("k=", n, " | Cross Validation Scores Mean:", scores.mean())