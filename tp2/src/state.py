from copy import deepcopy
from typing import List

import numpy as np

RED_CAR_INDEX = 0


class State:
    """
    Contructeur d'un état initial
    """

    def __init__(self, pos):
        """
        pos donne la position de la voiture i dans sa ligne ou colonne (première case occupée par la voiture);
        """
        self.pos = np.array(pos)
        self.index_of_last_moved_car = None
        self.last_move_direction = None
        self.previous_state = None
        self.nb_moves = 0
        self.score = 0

        # TODO
        self.rock = None

    def move(self, c, d) -> 'State':
        """
        Constructeur d'un état à partir du mouvement (c,d)
        """
        s = State(self.pos)
        s.previous_state = self
        s.pos[c] += d
        s.index_of_last_moved_car = c
        s.last_move_direction = d
        s.nb_moves = self.nb_moves + 1
        s.rock = self.rock
        return s

    def put_rock(self, rock_pos) -> 'State':
        s = State(self.pos)
        s.previous_state = self
        s.index_of_last_moved_car = self.index_of_last_moved_car
        s.last_move_direction = self.last_move_direction
        s.nb_moves = self.nb_moves
        s.rock = rock_pos
        return s

        new_state = deepcopy(self)
        new_state.previous_state = self
        new_state.rock = rock_pos
        return new_state

    def score_state(self, free_pos) -> None:
        """
        Elle affecte la valeur de l'état à son paramètre score. L'état n'est
        pas nécessairement final. Utiliser l'heuristique qui vous semble la
        plus pertinente.
        """
        self.score = self.score_heuristic_1(free_pos)

    def __red_car_pos_in_back(self) -> int:
        red_car_position = self.pos[0]
        return red_car_position

    def __get_impediments(self, free_pos: np.ndarray, length: List[int], move_on: List[int]) -> int:
        red_car = 0
        space_after_red_car = self.pos[0] + length[0]
        impediments = 0
        for i in range(space_after_red_car, len(free_pos[0])):
            if not free_pos[move_on[red_car]][i]:
                impediments += 1
        return impediments

    @staticmethod
    def __get_feeling_score(free_pos):
        x = [2, 1, -1, 2, 3, 4]
        score = 0
        for i in range(6):
            for j in range(6):
                if not free_pos[i][j]:
                    score += (6 - j) + x[i]
        return score

    def __score_len_3_vertical_cars(self, length: List[int], is_horizontal: List[int]) -> int:
        score = 0
        for i, (l, i_h) in enumerate(zip(length, is_horizontal)):
            if i_h or l is 2: continue
            score += (self.pos[i] + 1) * 2
        return score

    def __get_blocked_cars(self, free_pos: np.ndarray, length: List[int], move_on: List[int],
                           is_horizontal: List[int]) -> int:

        space_after_red_car = self.pos[0] + length[0]
        impediments = 0
        for i, (l, m_o, i_h) in enumerate(zip(length, move_on, is_horizontal)):
            if i_h or m_o < space_after_red_car:
                continue
            space_after_current_car = self.pos[i] + l
            space_before_current_car = self.pos[i] - 1

            def increment_if_inbound_and_occupied(space, col) -> bool:
                return 0 <= space < 6 and not free_pos[space][col]

            impediments += increment_if_inbound_and_occupied(space_after_current_car, m_o)
            impediments += increment_if_inbound_and_occupied(space_before_current_car, m_o)

        return impediments

    @staticmethod
    def is_inbound(i, j):
        return 0 <= i <= 5 and 0 <= j <= 5

    def __how_many_cars_touches_rock(self, free_pos: np.ndarray) -> int:
        if not self.rock:
            return 0

        x = self.rock[0]
        y = self.rock[1]
        count = 1 if self.is_inbound(x + 1, y) and not free_pos[x + 1][y] else 0
        count += 1 if self.is_inbound(x - 1, y) and not free_pos[x - 1][y] else 0
        count += 1 if self.is_inbound(x, y + 1) and not free_pos[x][y + 1] else 0
        count += 1 if self.is_inbound(x, y - 1) and not free_pos[x][y - 1] else 0
        return count

    def __how_many_car_positions_blocked_by_rock(self, length: List[int], move_on: List[int],
                                                 is_horizontal: List[int]) -> int:
        if not self.rock:
            return 0

        count = 0
        for i, (l, m_o, i_h) in enumerate(zip(length, move_on, is_horizontal)):
            if i_h:
                if m_o is self.rock[1]:
                    count += 1 if self.rock[0] is self.pos[i] - 1 else 0
                    count += 1 if self.rock[0] is self.pos[i] + l else 0
            else:
                if m_o is self.rock[0]:
                    count += 1 if self.rock[1] is self.pos[i] - 1 else 0
                    count += 1 if self.rock[1] is self.pos[i] + l else 0
        return count

    def __negative_feeling(self, free_pos: np.ndarray) -> int:
        feeling = 0

        for i in range(6):
            for j in range(self.pos[RED_CAR_INDEX] + 2, 6):
                feeling += not free_pos[i][j]

        return feeling

    def score_heuristic_1(self, visited, free_pos: np.ndarray, length: List[int], move_on: List[int],
                          is_horizontal: List[int]) -> int:
        nothing = 0

        impediment_penalty = 5
        block_penalty = 5

        negative_feeling_penalty = 1
        rock_touch_penalty = 1
        rock_block_penalty = 4

        visited_penalty = 100
        move_penalty = 25

        feeling_gain = 1
        vertical_3_gain = 2
        red_car_gain = 50
        win_gain = 5000

        penalty = nothing
        gain = nothing

        penalty += visited[hash(self)] * visited_penalty if hash(self) in visited else nothing
        penalty += impediment_penalty * self.__get_impediments(free_pos, length, move_on)
        penalty += block_penalty * self.__get_blocked_cars(free_pos, length, move_on, is_horizontal)
        penalty += rock_touch_penalty * self.__how_many_cars_touches_rock(free_pos)
        penalty += rock_block_penalty * self.__how_many_car_positions_blocked_by_rock(length, move_on, is_horizontal)
        penalty += negative_feeling_penalty * self.__negative_feeling(free_pos)
        penalty += move_penalty * self.nb_moves

        gain += red_car_gain * self.__red_car_pos_in_back()
        gain += feeling_gain * self.__get_feeling_score(free_pos)
        gain += vertical_3_gain * self.__score_len_3_vertical_cars(length, is_horizontal)
        gain += win_gain if self.success() else nothing

        self.score = gain - penalty
        return self.score

    def success(self):
        return self.pos[0] == 4

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        if len(self.pos) != len(other.pos):
            raise ValueError("les états n'ont pas le même nombre de voitures")

        return np.array_equal(self.pos, other.pos)

    def __hash__(self):
        h = 0
        for i in range(len(self.pos)):
            h = 37 * h + self.pos[i]
        return int(h)

    def __lt__(self, other):
        return self.score < other.score
