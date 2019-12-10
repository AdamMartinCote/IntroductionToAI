import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin


class SoftmaxClassifier(BaseEstimator, ClassifierMixin):
    nb_classes: int
    nb_features: int

    def __init__(self, lr=0.1, alpha=100, n_epochs=1000, eps=1.0e-5, threshold=1.0e-10, early_stopping=True):

        self.learning_rhythm = lr
        self.alpha = alpha
        self.n_epochs = n_epochs
        self.eps = eps
        self.threshold = threshold
        self.early_stopping = early_stopping

    def fit(self, X: np.ndarray, y=None) -> 'SoftmaxClassifier':
        """
            In:
            X : l'ensemble d'exemple de taille nb_example x nb_features
            y : l'ensemble d'étiquette de taille nb_example x 1

            Principe:
            Initialiser la matrice de poids
            Ajouter une colonne de bias à X
            Pour chaque epoch
                calculer les probabilités
                calculer le log loss
                calculer le gradient
                mettre à jouer les poids
                sauvegarder le loss
                tester pour early stopping

            Out:
            self, in sklearn the fit method returns the object itself
        """

        dim_y = X.shape[0]
        dim_x = X.shape[1]

        prev_loss = np.inf
        self.losses_ = []

        # self.nb_feature =
        # self.nb_classes =

        # X_bias =
        self.theta_weight_matrix = np.zeros(shape=(1, 1), dtype=np.float32)

        for epoch in range(self.n_epochs):

            # logits =
            # probabilities =

            # loss =
            # self.theta_ =

            if self.early_stopping:
                pass

        return self

    def predict_proba(self, X, y=None):
        try:
            getattr(self, "theta_")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        # X_bias =
        pass

    def predict(self, X, y=None):
        try:
            getattr(self, "theta_")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        pass

    def fit_predict(self, X, y=None):
        self.fit(X, y)
        return self.predict(X, y)

    def score(self, X, y=None, sample_weight=None):
        pass

    def _cost_function(self, probabilities, y):
        pass

    def _one_hot(self, y) -> np.array:
        dim = len(y)
        mat = np.zeros(shape=(dim, self.nb_classes))
        for idx, value in enumerate(y):
            mat[idx][value] = 1

        return mat

    def _softmax(self, z):
        pass

    def _get_gradient(self, X_bias, y, probas):

        pass
