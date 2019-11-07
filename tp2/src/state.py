from copy import deepcopy

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

    def __did_state_previously_happen(self) -> bool:
        state = self
        while state.previous_state is not None:
            state = state.previous_state
            if hash(state) is hash(self):
                return True
        return False

    def __did_red_car_advance(self) -> bool:
        positive_direction = 1
        return self.index_of_last_moved_car is RED_CAR_INDEX and self.last_move_direction is positive_direction

    def __did_red_car_backup(self) -> bool:
        negative_direction = -1
        return self.index_of_last_moved_car is RED_CAR_INDEX and self.last_move_direction is negative_direction

    def __is_red_car_on_winning_pos(self) -> bool:
        winning_pos = 4
        return self.pos[RED_CAR_INDEX] is winning_pos

    def __how_many_cars_touches_rock(self, free_pos: np.ndarray) -> int:
        if not self.rock:
            return 0

        def is_inbound(i, j):
            return 0 <= i <= 5 and 0 <= j <= 5

        x = self.rock[0]
        y = self.rock[1]
        count = 1 if is_inbound(x + 1, y) and not free_pos[x + 1][y] else 0
        count += 1 if is_inbound(x - 1, y) and not free_pos[x - 1][y] else 0
        count += 1 if is_inbound(x, y + 1) and not free_pos[x][y + 1] else 0
        count += 1 if is_inbound(x, y - 1) and not free_pos[x][y - 1] else 0
        return count

    def score_heuristic_1(self, free_pos: np.ndarray) -> int:
        nothing = 0
        small_penalty = 25
        big_penalty = 100
        big_gain = 100
        win_gain = 1000

        penalty = nothing
        gain = nothing

        penalty += big_penalty if self.__did_state_previously_happen() else nothing
        penalty += big_penalty if self.__did_red_car_backup() else nothing
        penalty += small_penalty * self.__how_many_cars_touches_rock(free_pos)

        gain += big_gain if self.__did_red_car_advance() else nothing
        gain += win_gain if self.__is_red_car_on_winning_pos() else nothing

        return gain - penalty

    def score_heuristic_2(self) -> float:
        """
        We use the ratio between the number of freepos in the left half of the grid
        vs the right half. More freepos on the right is better.

        Note: we might have to remove the red car from this score to avoid a bias as
        we move further right

        TODO: Not possible with current structure
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
