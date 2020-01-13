from time import time
from guang.Utils.toolsFunc import probar
from guang.Utils.plotly import Scatter3d
from guang.Utils.plotly import Subplots
from sklearn import manifold, datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

if __name__ == "__main__":
    n_points = 1500
    X, color = datasets.samples_generator.make_s_curve(n_samples=n_points, random_state=0)
    n_neighbors = 10
    n_components = 2

    fig = Scatter3d()
    fig.scatter3d(X[:,0], X[:, 1], X[:,2], mode="markers", color_marker=color)
    fig.show()

    methods = ['standard', 'ltsa', 'hessian','modified']
    labels = ['LLE', 'LTSA', 'Hessian LLE', 'Modified LLE']

    def LLE(X, method, n_neighbors=10, n_components=2):
        '''
        :param method 'standard', 'hessian', 'modified' or 'ltsa'
        '''
        Y = manifold.LocallyLinearEmbedding(n_neighbors, n_components,
                                            eigen_solver='auto',
                                            method=method).fit_transform(X)
        return Y

    fig = Subplots(2,5)
    for i, method in enumerate(methods):
        # if i>2:
        #     continue
        t0 = time()
        Y = LLE(X, method,n_neighbors, n_components)
        t1 = time()
        print("%s: %.2g sec" % (methods[i], t1 - t0))
        fig.plot(Y[:, 0], Y[:, 1], mode='markers', marker_color=color, marker_size=5,
                 label=f"{labels[i]}, {t1 - t0: .2g} sec")


    estimators = [(manifold.Isomap(n_neighbors, n_components), "Isomap"),
                  (manifold.MDS(n_components, max_iter=100, n_init=1), "MDS"),
                  (manifold.SpectralEmbedding(n_components=n_components,
                                              n_neighbors=n_neighbors), "Laplace Eigenmaps"),
                  (manifold.TSNE(n_components=n_components, init='pca', random_state=0), "t-SNE"),
                  (PCA(n_components), "PCA"),
                  (LDA(n_components=n_components), "LDA"),
                  ]

    for idx, (estimator_obj, estimator_name) in enumerate(estimators):
        # estimator_obj, estimator_name = estimator[0], estimator[1]
        t0 = time()
        if estimator_name=="LDA":
            Y = estimator_obj.fit_transform(X, (color).astype(int))
        else:
            Y = estimator_obj.fit_transform(X)
        t1 = time()
        print("%s: %.2g sec" % (estimator_name, t1 - t0))

        fig.plot(Y[:, 0], Y[:, 1],mode='markers', marker_color=color, marker_size=5,
                 label=f"{estimator_name}, {t1 - t0:.2g} sec")

    fig.show()