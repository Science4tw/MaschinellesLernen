import pandas as pd
from sklearn.model_selection import train_test_split

# load a file
data = pd.read_csv(
    "C:/Users/matth/OneDrive/W_Studium/00 Wirtschaftsinformatik/6 Business Intelligence/FS 2022/Teil 2 - Maschinelles Lernen/Termin 3 - Klassifikation mit Entscheidungsbäumen/census.data",
    header=None, index_col=False,
    names=['age', 'workclass', 'fnlwgt',
           'education', 'education-num',
           'marital-status', 'occupation',
           'relationship', 'race', 'gender',
           'capital-gain', 'capital-loss',
           'hours-per-week', 'native-country',
           'income'])

# transform categorical into binary features
data_n = pd.get_dummies(data)

# convert encoded DataFrame to NumPy arrays
X = data_n.loc[:, 'age':'native-country_ Yugoslavia'].values
y = data_n.loc[:, 'income_ <=50K'].values

# split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

"""aufgabe_1.py"""
from sklearn.tree import DecisionTreeClassifier

# load, transform, convert
# validation of parameters via grid search
best_score = 0
best_parameters = {}
for x in range(15, 26, 1):
    for y in range(10, 21, 1):
        tree = DecisionTreeClassifier(random_state=0,
        min_samples_leaf=x,
        max_depth=y)
        tree.fit(X_train, y_train)
        score = tree.score(X_test, y_test)

        # store the best score and parameters
        if score > best_score:
            best_score = score
            best_parameters = {"min_samples_leaf": x,
                                "max_depth": y}

print("Best score:", best_score)
print("Best parameters:", best_parameters)

