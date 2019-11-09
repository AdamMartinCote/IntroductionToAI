from tp2.src.minmaxsearch import MiniMaxSearch


class ExpectimaxSearch(MiniMaxSearch):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def solve_single_player(self, verbose=True):
        raise NotImplementedError("expectimax")

    def expectimax(self, current_depth, current_state, is_max):
        best_move = None
        return best_move

    def decide_best_move_expectimax(self, is_max):
        pass
