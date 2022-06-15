"""" aufgabe1.py"""
from sklearn import datasets
from sklearn.preprocessing import KBinsDiscretizer

# load dataset
ds = datasets.load_breast_cancer()
X, f = ds["data"], ds["feature_names"]
print("Numerischer Datensatz:")
print(X)

# equal frequency binning with 5 categories
binner = KBinsDiscretizer(n_bins=5, encode='ordinal',
    strategy='quantile')

binner.fit(X)
X_binned = binner.transform(X)
print("Kategorialer Datensatz:")
print(X_binned)

""" aufgabe2.py"""
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# load dataset
ds = datasets.load_breast_cancer()
X, y, f = ds["data"], ds["target"], ds["feature_names"]
# normalize data
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

# apply PCA
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

# plot first two components
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.show()


""" aufgabe3.py"""
from sklearn import datasets
from sklearn.feature_selection \
import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# load dataset
ds = datasets.load_breast_cancer()
X, y, f = ds["data"], ds["target"], ds["feature_names"]

# add 30 noisy features to the 30 original features
rng = np.random.RandomState(42)
noise = rng.normal(size=(len(X), 30))
X_with_noise = np.hstack([X, noise])

# feature selection withs sfs and Wrapper (kNN)
knn = KNeighborsClassifier(n_neighbors=1)
select = SequentialFeatureSelector(estimator=knn,
n_features_to_select=30)
select.fit(X_with_noise, y)
X_selected = select.transform(X_with_noise)

# visualize selection (black is selected, white not)
mask = select.get_support()
plt.matshow(mask.reshape(1, -1), cmap='gray_r')
plt.xlabel("Feature Index")
plt.show()

