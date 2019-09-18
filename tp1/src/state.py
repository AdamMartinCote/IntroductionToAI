import random
from typing import List

import numpy as np

from tp1.src.car import Car


class State:

    def __init__(self, pos, c=None, d=None, previous_state=None):
        """
        Contructeur d'un état initial
        pos donne la position de la voiture i (première case occupée par la voiture);
        """
        self.pos = np.array(pos, dtype=np.int64)

        """
        c, d et prev permettent de retracer l'état précédent et le dernier mouvement effectué
        """

        self.c = c
        self.d = d
        self.prev = previous_state
        self.h = 0

        try:
            self.nb_moves = previous_state.nb_moves + 1
        except AttributeError:
            self.nb_moves = 0

    def move(self, c: int, d: int) -> 'State':
        """
        Constructeur d'un état à partir mouvement (c,d)

        :param c: index of the car [0, nb_cars - 1]
        :param d: direction of the move [-1, 1]
        :return: State object
        """
        new_positions = np.copy(self.pos)
        new_positions[c] += d

        return State(new_positions, c, d, self)

    def success(self):
        """ est il final? """
        return self.pos[0] >= 4

    def estimee1(self) -> int:
        """
        Estimation du nombre de coup restants
        """
        red_car_position = self.pos[0]
        goal_position = 4
        return int(goal_position - red_car_position)

    def estimee2(self, free_pos: np.ndarray, cars: List[Car]) -> int:
        """
        Estimation du nombre de blocage entre l'auto rouge et la sortie
        """
        red_car = cars[0]
        space_after_red_car = self.pos[0] + red_car.length
        impediments = 0
        for i in range(space_after_red_car, len(free_pos[0])):
            if not free_pos[red_car.move_on_index][i]:
                impediments += 1
        return impediments * 2 + self.estimee1()

    def estimee3(self) -> int:
        return random.randint(1, 10)

    def __eq__(self, other: 'State') -> bool:
        if not isinstance(other, State):
            return NotImplemented
        if len(self.pos) != len(other.pos):
            raise Exception("les états n'ont pas le même nombre de voitures")

        return np.array_equal(self.pos, other.pos)

    def __hash__(self) -> int:
        h = 0
        for i in range(len(self.pos)):
            h = 37 * h + self.pos[i]
        return int(h)

    def __lt__(self, other: 'State') -> bool:
        return (self.nb_moves + self.h) < (other.nb_moves + other.h)
