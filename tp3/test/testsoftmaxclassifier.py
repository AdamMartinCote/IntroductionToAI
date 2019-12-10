from unittest import TestCase

import numpy as np

from tp3.softmax.softmaxclassifier import SoftmaxClassifier


class TestSoftmaxClassifier(TestCase):

    def setUp(self) -> None:
        self.softmax = SoftmaxClassifier()
        self.softmax.nb_classes = 6  # les classes possibles sont donc 0-5

    def testOneHot_diagonal_6_6(self):
        y1 = np.array([0, 1, 2, 3, 4, 5])
        y1.shape = (6, 1)
        one_hot = self.softmax._one_hot(y1)

        print('Premier test')
        print(one_hot)

        self.assertTrue(np.array_equal(one_hot,
                                       [[1, 0, 0, 0, 0, 0],
                                        [0, 1, 0, 0, 0, 0],
                                        [0, 0, 1, 0, 0, 0],
                                        [0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 1, 0],
                                        [0, 0, 0, 0, 0, 1]]
                                       ))

    def testOneHot_diagonal_4_1(self):
        y2 = np.array([5, 5, 5, 5])
        y2.shape = (4, 1)
        one_hot = self.softmax._one_hot(y2)

        print('\nDeuxième test')
        print(one_hot)
        self.assertTrue(np.array_equal(one_hot,
                                       [[0, 0, 0, 0, 0, 1],
                                        [0, 0, 0, 0, 0, 1],
                                        [0, 0, 0, 0, 0, 1],
                                        [0, 0, 0, 0, 0, 1]]
                                       ))

        # y3 = np.array([0, 0, 0, 0])
        # y3.shape = (4, 1)
        # print('\nTroisième test')
        # print(softmax._one_hot(y3))

        #
        # Troisième test
        # [[1. 0. 0. 0. 0. 0.]
        #  [1. 0. 0. 0. 0. 0.]
        #  [1. 0. 0. 0. 0. 0.]
        #  [1. 0. 0. 0. 0. 0.]]
