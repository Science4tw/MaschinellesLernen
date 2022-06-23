"""aufgabe.py"""
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas as pd
# load a file
data = pd.read_csv("C:/Users/matth/OneDrive/W_Studium/00 Wirtschaftsinformatik/6 Business Intelligence/"
                   "FS 2022/Teil 2 - Maschinelles Lernen/Termin 3 - Klassifikation mit Entscheidungsbäumen/census.data",
                    header=None, index_col=False,
                    names=['age', 'workclass', 'fnlwgt','education', 'education-num','marital-status', 'occupation',
                    'relationship', 'race', 'gender','capital-gain', 'capital-loss','hours-per-week','native-country',
                    'income'])

# transform categorical into binary features
data_n = pd.get_dummies(data)
# convert encoded DataFrame to NumPy arrays
X = data_n.loc[:, 'age':'native-country_ Yugoslavia'].values
y = data_n.loc[:, 'income_ <=50K'].values
# try n_neighbors from 1, 3, 5, ..., 39
neighbors_settings = range(1, 40, 2)
accuracies = []

for n in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n)
    scores = cross_val_score(knn, X, y, cv=5)
    accuracies.append(scores.mean())

# plot the results
plt.plot(neighbors_settings, accuracies,
label="crossvalidation accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()