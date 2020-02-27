'''
實驗1 - 其他變數固定, 調整perplexity 應該要看到分群分佈好的兩個極端，中間則是合適的perlexity
實驗2 - 其他變數固定, 調整input的dimension 64x64 -> 160x160 -> 300x300觀察
實驗3 - 其他變數固定, 看PCA壓縮到~50+ features

'''
import numpy as np
from sklearn.datasets import load_digits
from scipy.spatial.distance import pdist
from sklearn.manifold.t_sne import _joint_probabilities
from scipy import linalg
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import squareform
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
palette = sns.color_palette("bright", 10)


X, y = load_digits(return_X_y=True) # 載入數字資料, X 64 dimesion, data points 1797, y_label 1~10

tsne = TSNE()
X_embedded = tsne.fit_transform(X)

sns.scatterplot(X_embedded[:,0], X_embedded[:,1], hue=y, legend='full', palette=palette)

plt.show()