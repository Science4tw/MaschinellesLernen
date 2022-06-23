import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import complete
import matplotlib.pyplot as plt

# load a file
data = pd.read_csv("C:/Users/matth/OneDrive/W_Studium/00 Wirtschaftsinformatik/6 Business Intelligence/FS 2022/Teil 2 - Maschinelles Lernen/Termin 3 - Klassifikation mit Entscheidungsbäumen/census.data",
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

# first 100 data objects
X = X[0:100, :]

# normalize with mu-sigma method
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
# SciPy agglomerative clustering
linkage_array = complete(X)
# Plot the dendrogram
dendrogram(linkage_array, color_threshold=14.8)
plt.xlabel("Data Object")
plt.ylabel("Cluster distance")
plt.show()