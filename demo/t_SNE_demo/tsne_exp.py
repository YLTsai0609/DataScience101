'''
實驗1 - 其他變數固定, 調整perplexity 應該要看到分群分佈好的兩個極端，中間則是合適的perlexity - checked
實驗2 - 其他變數固定, 調整input的dimension 64x64 -> 160x160 -> 300x300觀察
實驗3 - 其他變數固定, 看PCA壓縮到~50+ features

one legen in many subplots
https://stackoverflow.com/questions/9834452/how-do-i-make-a-single-legend-for-many-subplots-with-matplotlib

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
import pandas as pd
sns.set(rc={'figure.figsize':(11.7,8.27)})
palette = sns.color_palette("bright", 10)
seed = 2

X, y = load_digits(return_X_y=True) # 載入數字資料, X 64 dimesion, data points 1797, y_label 1~10

# X, y = X[0:-1:10], y[0:-1:10]

# two cols
perplexity_list = [5, 10, 30, 40, 50, 70, 100, 200, 300]
fig, ax = plt.subplots(nrows=3,
                       ncols=3, figsize=(8,8))

for row_idx in range(3):
    for col_idx in range(3):
        per_idx = row_idx * 3 + col_idx
        print(row_idx, col_idx)
        tsne = TSNE(perplexity=perplexity_list[per_idx], random_state=seed)
        X_embedded = tsne.fit_transform(X)
        df = pd.DataFrame(X_embedded)
        X_cols = df.columns
        df['y'] = y
        grouped = df.groupby(by=['y'])
        for fig_idx, (_, grp) in enumerate(grouped):
            if per_idx == 0:
                partial_embedded_X = grp[X_cols].values
                y_label = grp['y'].unique().tolist()[0]
                color = palette[fig_idx]
                ax[row_idx][col_idx].scatter(partial_embedded_X[:,0], partial_embedded_X[:,1],
                        c = color,
                        label = y_label)
                ax[row_idx][col_idx].set_title(f"perplexity = {tsne.perplexity}\n iterations={tsne.n_iter}", fontsize=15)
                handles, labels = ax[row_idx][col_idx].get_legend_handles_labels()
                fig.legend(handles, labels, loc='upper right')
                # ax[row_idx][col_idx].legend()
            else:
                partial_embedded_X = grp[X_cols].values
                y_label = grp['y'].unique().tolist()[0]
                color = palette[fig_idx]
                ax[row_idx][col_idx].scatter(partial_embedded_X[:,0], partial_embedded_X[:,1],
                        c = color)
                ax[row_idx][col_idx].set_title(f"perplexity = {tsne.perplexity}\n iterations={tsne.n_iter}", fontsize=15)
plt.tight_layout()
plt.show()