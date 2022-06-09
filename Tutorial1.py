###############################################################################
""" Tutorial 1 - Basics """

# Regulärer Kommentar mit Hashtag #
""" docstring Kommentar """

""" Konventionen"""
# Pakete und Module: lowercase
# Funktionen und Variablen: lower case with underscores

# Funktionen
def print_meaning(answer):
    question = "Sinn des Lebens:"
    print(question, answer)

def add(op1, op2):
    result = op1 + op2
    print(result)

""" 1.2.1 Funktionen aufrufen """
# Funktionsaufruf
print_meaning("Zufriedenheit")
add(5, 10)

# Einzelne Funktion importieren: from modul_bezeichner import funktions_bezeichner
# Bibliothek importieren und Bezeichner ändern: import pandas as pd
# Modul aus Bibliothek importieren: from sklearn import datasets ODER import sklearn.datasets as ds

""" 1.2.2 Parameter an Funktionen Ubergeben """
def print_student(name, major="Informatik", semester=1):
    print(name, "studiert", major, "im", semester, "Semester")

print_student("Jakob")                      # Jakob studiert Informatik im 1 Semester
print_student("Mark", "Pharmazie")          # Mark studiert Pharmazie im 1 Semester
print_student("Mike", "Mathematik", 3)      # Mike studiert Mathematik im 3 Semester
print_student("John", semester=5)           # John studiert Informatik im 5 Semester
print_student("Sandra", major="Geologie")   # Sandra studiert Geologie im 1 Semester

""" 1.2.3 Listen und Wörterbucher """

squares = [1, 4, 9, 16, 25]
names = ["Maxime", "Emilie", "Noelle", "Eliane"]

# In Python durfen Listen Elemente verschiedener Datentypen enthalten
info = ["Alicia", 27, 1550.87]

# Mit Indizes k¨onnen wir auf einzelne Elemente zugreifen
val1 = squares[1] # gibt Wert 4 mit Index 1 zurück
val2 = squares[-1] # gibt Wert 25 mit Index 4 zurück

# 1. Sogenanntes Slicing gibt Teilbereiche einer Liste zuruck: listen_bezeichner[start:end:step]
# 2. Alle Slice-Operationen liefern eine Kopie der Liste mit den angeforderten Elementen
# vom Index start bis zum Index end (nicht inklusive) mit der gegebenen Schrittweite
# step.
# 3.1 Standardwert für start: 0
# 3.2 Standardwert für end: len(lst) Hinweis: len ist eine eingebaute Funktion und
# gibt die Länge der Liste lst zurück.
# 3.3 Standardwert für step: 1
squares = [1, 4, 9, 16, 25]
lst = squares[2:4] # [9, 16]
lst = squares[:3] # [1, 4, 9]
squares[2:] # [9, 16, 25]
squares[::2] # [1, 9, 25]
squares[:] # [1, 4, 9, 16, 25]}

# Zweidimensionale Listen besitzen Werte in zwei Dimensionen. Man kann sich zweidimensionale Listen
# als Tabellen mit Zeilen und Spalten vorstellen. Eine zweidimensionale Liste values mit drei Zeilen
# und zwei Spalten kann bspw. folgendermassen erstellt werden:
values = [[1, 2], [0, 2], [3, 7]]

# In zweidimensionalen Listen ben¨otigen wir zwei Indizes, um einen Wert anzusprechen
# (ein Index fur die Zeile und ein zweiter Index f ¨ ur die Spalte). Folgende Anweisung ¨
# weist der Variablen v den Wert zu, der im Array values in der dritten Zeile und
# der zweiten Spalte steht.
v = values[2][1] # 7
# Da zweidimensionale Listen eigentlich Listen von Listen sind, w¨are es korrekter zu
# sagen, dass wir mit values[2][1] den Wert mit Index 1 aus der Liste mit Index 2
# aus values referenzieren.

# Wir k¨onnen auch ganze “Zeilen” aus einer zweidimensionalen Liste auslesen
# (an jeder Position einer zweidimensionalen Liste befindet sich ja eine Liste):
row2 = values[2] # Liste an Position 2: [3, 7]

# Ein weiterer nutzlicher Datentyp, der in Python eingebaut ist, ist das Wörterbuch
# (dict). Am besten stellt man sich ein Wörterbuch als eine Menge von Schlüssel-
# Wert-Paare vor, mit der Anforderung, dass die Schlüssel eindeutig sind (innerhalb
# eines Wörterbuchs). Ein Klammerpaar erzeugt ein leeres Wörterbuch: {}. Durch
# Platzieren einer durch Kommas getrennten Liste von Schlüssel-Wert-Paaren inner-
# halb geschweifter Klammern werden dem W¨orterbuch anf¨anglich Elemente hinzugefugt.
# Die Schlüssel und die Werte werden dabei jeweils mit einem Doppelpunkt getrennt.
my_dict = {"Name":"John", "Alter":26}

# Die Hauptoperationen auf einem W¨orterbuch sind das Speichern eines Wertes mit irgendeinem Schlüssel
# und das Extrahieren des Wertes, bei einem gegebenen Schlüssel.
# Der Zugriff auf einen Wert aus einem W¨orterbuch funktioniert ¨ahnlich zu einem Zugriff in einer Liste.
# Statt dem Index gibt man aber innerhalb eckiger Klammern den Schlüssel an
age = my_dict["Alter"] # 26

# Wenn Sie in einem dict einen Wert unter Verwendung eines Schlüssel speichern,
# der bereits verwendet wird, wird der alte Wert, der mit diesem Schlüssel verbunden war,
# uberschrieben. Wenn Sie einen neuen Schlüssel verwenden, wird ein neues Schlüssel-
# Wert-Paar erstellt:
my_dict = {"Name":"John", "Alter":26}
my_dict["Alter"] = 37 # überschreiben
age = my_dict["Alter"] # 37
my_dict["Tel"] = 1234567 # neuer Schlüssel
tel = my_dict["Tel"] # 1234567

# Hinweis: Die Werte eines Schlussels k ¨ ¨onnen auch komplexere Datenstrukturen sein
# – z.B. Listen:
my_dict = {"o1":[1, 2, 3], "o2":[2, 3, 2]}
val = my_dict["o1"] # [1, 2, 3]

###############################################################################
