from copy import deepcopy

import numpy as np


class State:
    """
    Contructeur d'un état initial
    """

    def __init__(self, pos):
        """
        pos donne la position de la voiture i dans sa ligne ou colonne (première case occupée par la voiture);

        c,d et prev premettent de retracer l'état précédent et le dernier mouvement effectué

        """
        self.pos = np.array(pos)
        self.index_of_last_moved_car = None
        self.last_move_direction = None
        self.previous_state = None
        self.nb_moves = 0
        self.score = 0

        # TODO
        self.rock = None

    """
    Constructeur d'un état à partir du mouvement (c,d)
    """

    def move(self, c, d):
        s = State(self.pos)
        s.previous_state = self
        s.pos[c] += d
        s.index_of_last_moved_car = c
        s.last_move_direction = d
        s.nb_moves = self.nb_moves + 1
        # TODO
        return s

    def put_rock(self, rock_pos) -> 'State':
        new_state = deepcopy(self)
        new_state.previous_state = self
        new_state.rock = rock_pos
        return new_state

    def score_state(self):
        """
        Elle affecte la valeur de l'état à son paramètre score. L'état n'est
        pas nécessairement final. Utiliser l'heuristique qui vous semble la
        plus pertinente.
        """
        self.score = 0

    def score_heuristic_1(self) -> float:
        """
        We use the ratio between the number of freepos in the left half of the grid
        vs the right half. More freepos on the right is better.

        Note: we might have to remove the red car from this score to avoid a bias as
        we move further right
        """
        pass

    def success(self):
        return self.pos[0] == 4

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
        return self.score < other.score
