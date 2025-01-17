import sys

from tp2.src.state import State

MAX_RECURSION = 500


class MiniMaxSearch:
    def __init__(self, rushHour, initial_state, search_depth):

        sys.setrecursionlimit(MAX_RECURSION)

        self.rushhour = rushHour
        self.rushhour.state = initial_state
        self.search_depth = search_depth
        self.visited = dict()

    def minimax_1(self, current_depth: int, current_state: State) -> State or None:
        """
        Cette fonction contient la logique de l'algorithme minimax pour un
        seul joueur et retourne le meilleur coup à prendre à partir de l'état
        courant
        """
        self.rushhour.state = current_state

        possible_states = self.rushhour.get_possible_moves()
        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = - (sys.maxsize - 1)
        best_state = None
        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.minimax_1(current_depth + 1, possible_state)
            tmp_state.score += current_score
            if tmp_state is None: continue
            if current_state.score < tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state

        return best_state if current_depth is 0 else current_state

    def min_value(self, current_depth, current_state):

        self.rushhour.state = current_state

        possible_states = self.rushhour.possible_rock_moves()

        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = sys.maxsize
        best_state = None

        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.max_value(current_depth + 1, possible_state)
            tmp_state.score += current_score
            if current_state.score > tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state

        return best_state if current_depth is 0 else current_state

    def max_value(self, current_depth, current_state):
        # if hash(current_state) in self.visited:
        #     if self.visited[hash(current_state)] % 2:
        #         return None

        self.rushhour.state = current_state

        possible_states = self.rushhour.get_possible_moves()

        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = - (sys.maxsize - 1)
        best_state = None
        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.min_value(current_depth + 1, possible_state)
            tmp_state.score += current_score
            if current_state.score < tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state

        return best_state if current_depth is 0 else current_state

    def minimax_2(self, current_depth, current_state, is_max):
        return self.max_value(current_depth, current_state) if is_max else self.min_value(current_depth, current_state)

    def min_pruning(self, current_depth, current_state, alpha, beta):
        self.rushhour.state = current_state

        possible_states = self.rushhour.possible_rock_moves()

        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = sys.maxsize
        best_state = None

        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.max_pruning(current_depth + 1, possible_state, alpha, beta)
            tmp_state.score += current_score
            if current_state.score > tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state
            beta = min(beta, current_state.score)
            if alpha >= beta: break

        return best_state if current_depth is 0 else current_state

    def max_pruning(self, current_depth, current_state, alpha, beta):
        self.rushhour.state = current_state

        possible_states = self.rushhour.get_possible_moves()

        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = - (sys.maxsize - 1)
        best_state = None
        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.min_pruning(current_depth + 1, possible_state, alpha, beta)
            tmp_state.score += current_score
            if current_state.score < tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state
            alpha = max(alpha, current_state.score)
            if alpha >= beta: break

        return best_state if current_depth is 0 else current_state

    def max_exp_value(self, current_depth, current_state):
        # if hash(current_state) in self.visited:
        #     if self.visited[hash(current_state)] % 2:
        #         return None

        self.rushhour.state = current_state

        possible_states = self.rushhour.get_possible_moves()

        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = - (sys.maxsize - 1)
        best_state = None
        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.exp_value(current_depth + 1, possible_state)
            tmp_state.score += current_score
            if current_state.score < tmp_state.score:
                current_state.score = tmp_state.score
                best_state = tmp_state

        return best_state if current_depth is 0 else current_state

    def exp_value(self, current_depth, current_state):

        self.rushhour.state = current_state

        possible_states = self.rushhour.possible_rock_moves()
        p = 1 / len(possible_states)
        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = 0

        tmp_states = []

        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.max_value(current_depth + 1, possible_state)
            current_state.score += current_score + tmp_state.score * p
            tmp_states.append(tmp_state)

        import random
        random_index = random.randrange(len(tmp_states))
        random_state = tmp_states[random_index]
        random_state.score = current_state.score

        return random_state if current_depth is 0 else current_state

    def exp_value_optimistic(self, current_depth, current_state):

        self.rushhour.state = current_state

        possible_states = self.rushhour.possible_rock_moves()
        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = 0

        tmp_states = []

        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.max_value(current_depth + 1, possible_state)
            tmp_states.append(tmp_state)

        scores = [t_s.score + current_score for t_s in tmp_states]
        sum_score = sum(scores)
        ps = [1-(score / sum_score) for score in scores]

        for p, score in zip(ps, scores):
            current_state.score += score * p

        import random
        random_index = random.randrange(len(tmp_states))
        random_state = tmp_states[random_index]
        random_state.score = current_state.score

        return random_state if current_depth is 0 else current_state

    def exp_value_pessimistic(self, current_depth, current_state):

        self.rushhour.state = current_state

        possible_states = self.rushhour.possible_rock_moves()
        current_state.score_heuristic_1(self.visited, self.rushhour.free_pos, self.rushhour.length,
                                        self.rushhour.move_on, self.rushhour.horiz)

        current_score = current_state.score

        if current_depth is self.search_depth or current_state.success():
            return current_state

        current_state.score = 0

        tmp_states = []

        for possible_state in possible_states:
            possible_state.previous_state = None
            possible_state.nb_moves -= 1  # because it adds one in get_possible_moves
            tmp_state = self.max_value(current_depth + 1, possible_state)
            tmp_states.append(tmp_state)

        scores = [t_s.score + current_score for t_s in tmp_states]
        sum_score = sum(scores)
        ps = [score / sum_score for score in scores]

        for p, score in zip(ps, scores):
            current_state.score += score * p

        import random
        random_index = random.randrange(len(tmp_states))
        random_state = tmp_states[random_index]
        random_state.score = current_state.score

        return random_state if current_depth is 0 else current_state

    def minimax_pruning(self, current_depth, current_state, is_max, alpha, beta):
        return self.max_pruning(current_depth, current_state, alpha, beta) if is_max \
            else self.min_pruning(current_depth, current_state, alpha, beta)

    def expectimax(self, current_depth, current_state, is_max, exp_func):
        return self.max_exp_value(current_depth, current_state) if is_max \
            else exp_func(current_depth, current_state)

    def decide_best_move_1(self):
        """
        Cette fonction trouve et exécute le meilleur coup pour une partie à un joueur
        """
        # todo: this is a try
        init_state = self.rushhour.state
        best_move = self.minimax_1(0, self.rushhour.state)
        self.rushhour.state = init_state
        self.rushhour.update_free_pos()
        if hash(init_state) not in self.visited:
            self.visited[hash(init_state)] = 1
        else:
            self.visited[hash(init_state)] += 1
        self.rushhour.state = init_state.move(best_move.index_of_last_moved_car,
                                              best_move.last_move_direction)

    def decide_best_move_2(self, is_max):
        init_state = self.rushhour.state
        best_move = self.minimax_2(0, self.rushhour.state, is_max)
        self.rushhour.state = init_state
        self.rushhour.update_free_pos()

        if is_max:
            self.rushhour.state = init_state.move(best_move.index_of_last_moved_car,
                                                  best_move.last_move_direction)
        else:
            self.rushhour.state = init_state.put_rock(best_move.rock)
            if hash(init_state) not in self.visited:
                self.visited[hash(init_state)] = 1
            else:
                self.visited[hash(init_state)] += 1

    def decide_best_move_pruning(self, is_max):
        init_state = self.rushhour.state
        best_move = self.minimax_pruning(0, self.rushhour.state, is_max, - (sys.maxsize - 1), sys.maxsize)
        self.rushhour.state = init_state
        self.rushhour.update_free_pos()

        if is_max:
            self.rushhour.state = init_state.move(best_move.index_of_last_moved_car,
                                                  best_move.last_move_direction)
        else:
            self.rushhour.state = init_state.put_rock(best_move.rock)
            if hash(init_state) not in self.visited:
                self.visited[hash(init_state)] = 1
            else:
                self.visited[hash(init_state)] += 1

    def decide_best_move_expectimax(self, is_max, is_pessimistic=False, is_optimistic=False):
        init_state = self.rushhour.state
        best_move = None

        if is_pessimistic:
            best_move = self.expectimax(0, self.rushhour.state, is_max, self.exp_value_pessimistic)
        elif is_optimistic:
            best_move = self.expectimax(0, self.rushhour.state, is_max, self.exp_value_optimistic)
        else:
            best_move = self.expectimax(0, self.rushhour.state, is_max, self.exp_value)

        self.rushhour.state = init_state
        self.rushhour.update_free_pos()

        if is_max:
            self.rushhour.state = init_state.move(best_move.index_of_last_moved_car,
                                                  best_move.last_move_direction)
        else:
            self.rushhour.state = init_state.put_rock(best_move.rock)
            if hash(init_state) not in self.visited:
                self.visited[hash(init_state)] = 1
            else:
                self.visited[hash(init_state)] += 1

    def solve_single_player(self, verbose=True) -> None:
        while not self.rushhour.state.success():
            self.decide_best_move_1()
            s = self.str_move(True, self.rushhour.state)
            if verbose:
                self.rushhour.plot_free_pos()
                print(s)

    def solve_two_players(self, verbose=True):
        is_max = True
        while not self.rushhour.state.success():
            self.decide_best_move_2(is_max)
            s = self.str_move(is_max, self.rushhour.state)

            is_max = not is_max

            if verbose:
                self.rushhour.plot_free_pos()
                print(s)

    def solve_pruning(self, verbose=True):
        is_max = True
        while not self.rushhour.state.success():
            self.decide_best_move_pruning(is_max)
            s = self.str_move(is_max, self.rushhour.state)

            is_max = not is_max

            if verbose:
                self.rushhour.plot_free_pos()
                print(s)

    def solve_expectimax(self, verbose=True, is_pessimistic=False, is_optimistic=False):
        is_max = True
        while not self.rushhour.state.success():
            self.decide_best_move_expectimax(is_max, is_pessimistic, is_optimistic)
            s = self.str_move(is_max, self.rushhour.state)

            is_max = not is_max

            if verbose:
                self.rushhour.plot_free_pos()
                print(s)

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
