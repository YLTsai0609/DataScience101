'''
TSNE - 大部分參數會造成什麼效果都已經在這裡說明了
https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html

這裡特別說明perprexity的大小如何影響embedding
https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html#sphx-glr-auto-examples-manifold-plot-t-sne-perplexity-py

這裡說明了tSNE的一些參數調整以及結果解釋需要注意的地方
https://mropengate.blogspot.com/2019/06/t-sne.html

perplexity : 可以視為平滑過後的有效鄰居數，這個值用於取得Similarity func中的sigma
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