import numpy as np
import math
import copy


class State:
    """
    Contructeur d'un état initial
    """

    def __init__(self, pos, c=None, d=None, previous_state=None):
        """
        pos donne la position de la voiture i (première case occupée par la voiture);
        """
        self.pos = np.array(pos)

        """
        c, d et prev premettent de retracer l'état précédent et le dernier mouvement effectué
        """

        # self.c = self.d = self.prev = None
        self.c = c
        self.d = d
        self.prev = previous_state

        self.nb_moves = previous_state.nb_moves + 1
        self.h = 0

    """
    Constructeur d'un état à partir mouvement (c,d)
    """

    def move(self, c, d):
        """

        :param c: index of the car [0, 5]
        :param d: direction of the move [-1, 1]
        :return: State object
        """
        # TODO
        new_positions = self.pos[:]
        new_positions[c] += d

        return State(new_positions, c, d, self)


    def success(self):
        """ est il final? """
        # TODO
        return self.pos[0] >= 4

    """
    Estimation du nombre de coup restants 
    """

    def estimee1(self):
        # TODO
        return 0

    def estimee2(self, rh):
        # TODO
        return 0

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        if len(self.pos) != len(other.pos):
            print("les états n'ont pas le même nombre de voitures")

        return np.array_equal(self.pos, other.pos)

    def __hash__(self):
        h = 0
        for i in range(len(self.pos)):
            h = 37 * h + self.pos[i]
        return int(h)

    def __lt__(self, other):
        return (self.nb_moves + self.h) < (other.nb_moves + other.h)