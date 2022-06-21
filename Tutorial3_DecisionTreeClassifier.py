""" demo Entscheidungsbäume """
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# laden eines integrierten Datensatzes
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

# Lernen eines ungestutzten Baumes
tree = DecisionTreeClassifier(criterion="gini", random_state=42)
# citerion=.. -> Kriterium zur Wahl des "besten" Attributs z.B. mit Gini Index
tree.fit(X_train, y_train) # fit -> lernen -> an der Trainingsmenge anpassen/lernen
print("(Erkennungsrate) Accuracy tree on training set:", tree.score(X_train, y_train)) # 100% -> Logisch, kein
# pruning und auf der Traingsmenge, welche bereits gelernt wurde.

print("(Erkennungsrate) Accuracy tree on test set:", tree.score(X_test, y_test))


# visualize the tree (open in omnigraffle or similar)
export_graphviz(tree, out_file="tree_unpruned.dot", feature_names=cancer["feature_names"],
               impurity=False, filled=True) # dot File Format

# Stutzen des Baums (pruning) -> Möchte Baum lernen lassen
tree_pruned = DecisionTreeClassifier(criterion="gini", random_state=42, max_depth=4)
# max_depth=.. -> Maximale Tiefe des Baums, also maximale Anzahl Entscheidungen bis klassifiziert wird
tree_pruned.fit(X_train, y_train)
print("(Erkennungsrate) Accuracy tree on training set:", tree_pruned.score(X_train, y_train)) # Sinkt auf Trainingsm.
print("(Erkennungsrate) Accuracy tree on test set:", tree_pruned.score(X_test, y_test)) # Steigt dafür auf Testmenge
# Fazit: Müssen das Stutzen des Baums so hinkriegen, dass wir sweat spot finden zwischen overfitting und underfitting

""" Systematische Vorgehensweise mit For-Schleifen (syntaktisch zimlicher Unterschied zu Java^^) """

# 2 Automatisierung der Ausgabe mit bester Erkennungsrate und Parameter
best_score = 0
best_parameter = {}

# 1 Validation of parameter via grid search -> ERHALTE X*Y MODELLLE und bewerte diese jeweils!!
for x in [0.0001, 0.001, 0.01, 0.1]:
    for y in [3, 4, 5, 6, 7, 8, 9, 10]:
        # Definiere einen DecisionTree für jede Kombination aus x und y
        # y -> für maximale Tiefe bzw. Anzahl Entscheidungen
        # x -> Impurity=Unreinheit -> wie starke Unreinheit  abnehmen muss
        # Nun hab ich mit x und y 2 Variablen, welche mir das Stutzen des Baums steuern
        tree_pruned_systematisch = DecisionTreeClassifier(criterion="gini", random_state=42,
                                                          max_depth=y, min_impurity_decrease=x)

        # Mit dieser For-Schleife kriege ich x*y verschiedene Entscheidungsbäume, welche ich nun trainiere
        tree_pruned_systematisch.fit(X_train, y_train)

        # Teste die Erkennungsrate auf dem Testset
        score = tree_pruned_systematisch.score(X_test, y_test)

        # Ausgeben der Resulate der x*y Bäume
        # print("Unreinheit" + x, "Maximale Tiefe:" + y, "Erkennungsrate Test set:" + score)

        # 2
        if score >= best_score:
            best_score = score
            best_parameter = {"min_impurity_decrease":x, "max_depth":y}

print("Best Score:", best_score)
print("Best Parameters", best_parameter)




