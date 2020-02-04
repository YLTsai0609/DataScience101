# +
# Running this .py file using jupyter notebook with jupytext

# Reference

# plot-dendrogram-using-sklearn-agglomerativeclustering
# https://stackoverflow.com/questions/29127013/plot-dendrogram-using-sklearn-agglomerativeclustering

# Dendrogram or Other Plot from Distance Matrix
# https://stackoverflow.com/questions/41416498/dendrogram-or-other-plot-from-distance-matrix

# More Usage about dendrogram
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

# +
# Authors: Mathew Kallada
# License: BSD 3 clause
"""
=========================================
Plot Hierarachical Clustering Dendrogram 
=========================================
This example plots the corresponding dendrogram of a hierarchical clustering
using AgglomerativeClustering and the dendrogram method available in scipy.
"""

import numpy as np
import pandas as pd
import numpy.linalg as LA
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns

sns.set(font_scale=1.68)

def plot_dendrogram(model, **kwargs):

    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0]+2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)
    print(linkage_matrix.shape, linkage_matrix)

    # Plot the corresponding dendrogram
    fig, ax = plt.subplots(figsize=(15,7))
    dendrogram(linkage_matrix, ax=ax, no_plot=False,**kwargs)
    plt.title('Hierarchical Clustering Dendrogram')
    


iris = load_iris()
x = iris.data[:20]
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)


model = model.fit(x)

plot_dendrogram(model, labels=model.labels_)
# -

model.__dict__

model.children_.shape

# +
lbl_c = pd.Series(model.labels_).astype(str)
lbl_idx = pd.Series(np.arange(20)).astype(str)

lbl_c_idx_x = lbl_c.str.cat(lbl_idx, join='left', sep='_').values
# -

lbl_c_idx_x

plot_dendrogram(model, labels=lbl_c_idx_x)





import numpy as np
import numpy.linalg as LA

x

print(LA.norm(x[0] - x[1]))
print(LA.norm(x[1] - x[2]))
print(LA.norm(x[1] - x[3]))
print(LA.norm(x[14] - x[15]))


def caculate_dist_matrix(features : 'np.array (N, Z)') -> 'np.array (N, N)':
    nrof_images = features.shape[0]
    matrix = np.zeros((nrof_images, nrof_images))
    for i in range(nrof_images):
        for j in range(nrof_images):
            matrix[i][j] = LA.norm(features[i] - features[j])
    return matrix


d = caculate_dist_matrix(x)
d.shape

# +
model_2 = AgglomerativeClustering(distance_threshold=0, n_clusters=None)


model_2 = model.fit(d)

# plot_dendrogram(model, labels=model.labels_)
# -

model_2.__dict__

# +
from scipy.spatial.distance import squareform

be_tested = d[0:4, 0:4]
condensed_d = squareform(be_tested)

squareform(condensed_d) # shoud back to original d
display(be_tested, condensed_d, squareform(condensed_d))

# +
import numpy as np

from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

import matplotlib.pyplot as plt


mat = np.array([[0.0, 2.0, 0.1], [2.0, 0.0, 2.0], [0.1, 2.0, 0.0]])
dists = squareform(mat)
linkage_matrix = linkage(dists, "single")
print(linkage_matrix, type(linkage_matrix))
dendrogram(linkage_matrix, labels=["0", "1", "2"])
plt.title("test")
plt.show()
# -

dists = squareform(d)
lbl = [f"{i}" for i in range(d.shape[0])]
linkage_matrix = linkage(dists, "single")
print(linkage_matrix, type(linkage_matrix))
dendrogram(linkage_matrix, labels=lbl)
plt.title("iris")
plt.show()


