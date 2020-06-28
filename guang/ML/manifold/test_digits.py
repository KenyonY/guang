from guang.Utils.toolsFunc import probar
from guang.Utils.plotly import Scatter3d
from guang.Utils.plotly import Subplots
import plotly.graph_objects as go
import plotly.express as px
from sklearn import manifold, datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import numpy as np
from guang.Utils.plotly import imshow

from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

if __name__ == "__main__":
    digits = load_digits()
    data = digits.data
    print(data.shape)

    X = np.vstack([digits.data[digits.target == i] for i in range(10)])
    color = np.hstack([digits.target[digits.target == i] for i in range(10)])

    n_neighbors = 10
    n_components = 2

    def LLE(method, n_neighbors=10, n_components=2):
        '''
        :param method 'standard', 'hessian', 'modified' or 'ltsa'
        '''
        Y = manifold.LocallyLinearEmbedding(n_neighbors,
                                            n_components,
                                            eigen_solver='auto',
                                            method=method)
        return Y

    estimators = [(manifold.Isomap(n_neighbors, n_components), "Isomap"),
                  (manifold.MDS(n_components, max_iter=100, n_init=1), "MDS"),
                  (manifold.SpectralEmbedding(n_components=n_components,
                                              n_neighbors=n_neighbors),
                   "Laplace Eigenmaps"),
                  (manifold.TSNE(n_components=n_components,
                                 init='pca',
                                 random_state=0), "t-SNE"),
                  (PCA(n_components), "PCA"), (LLE(method='standard'), 'LLE'),
                  (LLE(method='modified'), 'modified LLE')]
    # data == X
    img = X[0, :].reshape(8, 8)

    fig = Subplots(2, 4)
    for idx, i in probar(estimators):
        print(i[1])
        target = i[0].fit_transform(X)
        fig.plot(target[:, 0],
                 target[:, 1],
                 mode='markers',
                 marker_color=color,
                 label=i[1])

    fig.show()

    fig = imshow(img)
    fig.show()
