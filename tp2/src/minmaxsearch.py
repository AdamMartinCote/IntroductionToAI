class MiniMaxSearch:
    def __init__(self, rushHour, initial_state, search_depth):
        self.rushhour = rushHour
        self.state = initial_state
        self.search_depth = search_depth

    def minimax_1(self, current_depth, current_state):
        # TODO
        best_move = None
        return best_move

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
        pass # TODO

    def decide_best_move_2(self, is_max):
        pass # TODO

    def decide_best_move_pruning(self, is_max):
        pass # TODO

    def decide_best_move_expectimax(self, is_max):
        pass # TODO

    def solve(self, state, is_singleplayer):
        pass # TODO

    def print_move(self, is_max, state):
        pass # TODO

