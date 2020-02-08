import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF

X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])

model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_
print('NMF')
print(X.shape ,W.shape, H.shape)
print('')
print(W)
print('')
print(H)

print('')
print('PCA')
pca = PCA(n_components=2)
pca.fit(X)

print(pca.explained_variance_ratio_)
print('')
print(pca.singular_values_)
print('')
print('PCs')
print(pca.components_)