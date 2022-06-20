""" demo of neural network"""
# X_train ->    Trainingsdatensatz
# X_test ->     Testdatensatz
# Y_train ->    Trainingslabel
# Y_test ->     Testlabel
# MLP ->        Multi Layer Perceptron (-> Feedforward Perceptron Netz)

# load an integrated dataset
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

# split in train set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target,
                                                    random_state=77)
# train_test_split: 1 Parameter: Daten | 2P: Zielvariable | 3P: stratify -> Klassenzugehörigkeit wird berücksichtigt
# (auf der Zielvariable) | 4P: random_state -> Mache das ganze reproduzierbar (Selbes Ergebnis beim nächsten Start des
# Programms, wenn man irgendeine Zahl zuweist)

# Importieren eines neuronalen Netzes mit einem MLPClassifier. Mit diesem Classifier können wir das NN gleich, wie
# im Skript erläutert trainieren.
from sklearn.neural_network import MLPClassifier

# Instanziieren des MLPClassifier
mlp = MLPClassifier()
# Mögliche Parameter:
# max_iter=.. _> maximale Anzahl Epochen (Iterationen)
# learning_rate=.. -> Wie stark das Gewicht angepasst werden soll (c im Algorithmus, umso grösser desto brachialer)
# activation=.. -> Aktivierungsfunktion (default: activation=relu) ( oder z.B. Binary Step, identity
# Architektur des NN:
# hidden_layer_sizes=(20, 10, 5)  -> Versteckte Layer, 1P: z.B. 20 Neuronen (Knoten) in der ersten Schicht,
# 10 in der zweiten etc.)

# Instanziieren eines neuronalen Netzes

# Trainieren eines neuronalen Netzes auf der Trainingsmenge (Wie bei allen Klassifikatoren mit fit()=
mlp.fit(X_train, Y_train)
# 1P -> Daten | 2P -> Label

# Vorhersagen der Klassenzugehörigkeit auf der Testmenge in Liste speichern
predictions_Class = mlp.predict((X_test))
# Ausgeben der Vorhersagen
print(predictions_Class) # Ausgabe [ 1 0 0 ....

# Vorhersagen der Klassenzugehörigkeit und der Ausgabe Wahrscheinlichkeit jedes Neurons (Winner takes all Prinzip))
predictions_ClassAndProba = mlp.predict_proba((X_test))
print(predictions_ClassAndProba)
# Ausgabe der ersten 3 Objekte kommentiert, wie oberhalb auch wo nur Klasse ausgegeben wird
# [[ 3.04552653e-02 9.69544735e-01] -> Klasse 1
# [9.99999866e-01 1.34438058e-07] -> Klasse 0
# [9.99998892e-01 1.10779517e-06] -> Klasse 0

# Wie bisher gewohnt, könnten wir die Erkennungsrate der Klassifikation
# auch einfach mit classifier.score(X_test, Y_test) ausgeben
print("Erkennungsrate (Accuracy) mlp :", mlp.score(X_test, Y_test))
# Hätte in diesem Beispiel 90% ohne das wir an den Parametern etwas "tunen"

# Test bzw. Training mit z.B x,y,.. versteckten Neuronen
# (könnte man nahezu endlos ausprobieren, deshalb systematisch vorgehen! -> automatisieren mit z.B.
# For Schleife und div. Architekturen ausprobieren)
mlp1 = MLPClassifier(hidden_layer_sizes=(100,50))
mlp1.fit(X_train, Y_train)
print("Erkennungsrate (Accuracy) mlp1:", mlp1.score(X_test, Y_test))