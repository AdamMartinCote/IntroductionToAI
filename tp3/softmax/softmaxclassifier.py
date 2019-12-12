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

        m = X.shape[0]
        n = X.shape[1]
        k = self.nb_features

        X_bias = np.zeros(shape=(m, n + 1))
        X_bias[:, :1] = 1

        self.theta_weight_matrix = np.random.rand(n + 1, k)

        prev_loss = np.inf
        self.losses_ = []

        self.nb_features = n

        for epoch in range(self.n_epochs):

            # logits =
            probabilities = self.predict_proba(X_bias, y)

            loss = self._cost_function(probabilities, y)
            self.theta_weight_matrix -= self.learning_rhythm * self._get_gradient(X_bias, y, probabilities)

            if self.early_stopping:
                if np.abs(prev_loss - loss) < self.threshold:
                    break
                prev_loss = loss

        return self

    def predict_proba(self, X, y=None):
        try:
            getattr(self, "theta_weight_matrix")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")

        m = X.shape[0]
        n = X.shape[1]
        # X_bias = np.zeros(shape=(m, n + 1))

        X_bias = np.concatenate((np.ones((m, 1), dtype=float), X), axis=1)
        Z = X_bias @ self.theta_weight_matrix
        return np.array([self._softmax(z) for z in Z])

    def predict(self, X, y=None):
        try:
            getattr(self, "theta_weight_matrix")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        P = self.predict_proba(X, y)
        return [np.argmax(p) for p in P]

    def fit_predict(self, X, y=None):
        self.fit(X, y)
        return self.predict(X, y)

    def score(self, X, y=None, sample_weight=None) -> float:
        prob = self.predict_proba(X, y)
        return self._cost_function(prob, y)

    def _cost_function(self, probabilities, y):
        encoded_y = self._one_hot(y)
        P_mat = np.clip(probabilities, self.eps, 1 - self.eps)

        return (-1.0) / len(y) * np.sum(encoded_y * np.log(P_mat))

    def _one_hot(self, y) -> np.array:
        size = (len(y), self.nb_classes)
        ret = np.zeros(size, dtype=float)
        for i in range(len(y)):
            ret[i][y[i]] = 1.0
        return ret

    def _softmax(self, z):
        z_exp = [np.exp(z_j) for z_j in z]
        z_exp_sum = np.sum(z_exp)
        return [z_exp[i] / z_exp_sum for i in range(len(z_exp))]

    def _get_gradient(self, X_bias, y, probas):
        m = len(y)
        y_ohe = self._one_hot(y)
        return (1 / m) * X_bias.T @ (probas - y_ohe)
