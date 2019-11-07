import sys

from tp2.src.rushhour import RushHour
from tp2.src.state import State

MAX_RECURSION = 500


class MiniMaxSearch:
    def __init__(self, rushHour, initial_state, search_depth):

        sys.setrecursionlimit(MAX_RECURSION)

        self.rushhour = rushHour
        self.rushhour.state = initial_state
        self.search_depth = search_depth
        self.visited = set()

    def minimax_1(self, current_depth: int, current_state: State) -> State or None:
        """
        Cette fonction contient la logique de l'algorithme minimax pour un
        seul joueur et retourne le meilleur coup à prendre à partir de l'état
        courant
        """
        # todo: je suis vraiment pas certain de ca
        if hash(current_state) in self.visited:
            return None

        tmp_rushhour: RushHour = self.rushhour

        tmp_rushhour.state = current_state

        possible_states = tmp_rushhour.get_possible_moves()

        if current_depth is self.search_depth:
            current_state.score_heuristic_1(tmp_rushhour.free_pos, tmp_rushhour.length,
                                            tmp_rushhour.move_on, tmp_rushhour.horiz)
            return current_state

        current_state.score = - (sys.maxsize - 1)
        best_state = None
        for possible_state in possible_states:
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.minimax_1(current_depth + 1, possible_state)
            if tmp_state is None: continue
            if current_state.score < tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state

        return best_state if current_depth is 0 else current_state

    def min_value(self, current_depth, current_state):
        pass

    def max_value(self, current_depth, current_state):
        pass

    def minimax_2(self, current_depth, current_state, is_max):
        # TODO
        best_move = None
        return best_move

    def minimax_pruning(self, current_depth, current_state, is_max, alpha, beta):
        # TODO
        best_move = None
        return best_move

    def expectimax(self, current_depth, current_state, is_max):
        # TODO
        best_move = None
        return best_move

    def decide_best_move_1(self):
        """
        Cette fonction trouve et exécute le meilleur coup pour une partie à un joueur
        """
        # todo: this is a try
        best_move = self.minimax_1(0, self.rushhour.state)
        self.visited.add(hash(self.rushhour.state))
        print(self.str_move(True, best_move))
        print(best_move.score)
        self.rushhour.state = self.rushhour.state.move(best_move.index_of_last_moved_car,
                                                       best_move.last_move_direction)

    def decide_best_move_2(self, is_max):
        pass  # TODO

    def decide_best_move_pruning(self, is_max):
        pass  # TODO

    def decide_best_move_expectimax(self, is_max):
        pass  # TODO

    def solve_1(self, verbose=True):
        while not self.rushhour.state.success():
            self.decide_best_move_1()
            s = self.str_move(True, self.rushhour.state)
            if verbose:
                print(s)

    def solve_2(self, state):
        pass

    def str_move(self, is_car, state):
        message = ''
        if is_car:
            car_index = state.index_of_last_moved_car
            color = self.rushhour.color[car_index]
            is_horiz = self.rushhour.horiz[car_index]
            d = state.last_move_direction
            dir = ''
            if is_horiz:
                dir = 'la droite' if d is 1 else 'la gauche'
            else:
                dir = 'le bas' if d is 1 else 'le haut'
            message = f'Voiture {color} vers {dir}'
        else:
            rock = state.rock
            message = f'Roche dans la case {rock[0]}-{rock[1]}'

        return message
