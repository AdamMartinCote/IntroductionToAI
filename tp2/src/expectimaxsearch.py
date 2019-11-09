from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.state import State


class ExpectimaxSearch(MiniMaxSearch):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def solve_single_player(self, verbose=True):
        raise NotImplementedError("expectimax")

    def execute_expectimax(self, current_depth, current_state, is_max):
        best_move = None
        return best_move

    def get_expectimax_value(self):
        state: State = self.rushhour.state
        if state.success():
            return self.mesure_state_utility(state)

    def mesure_state_utility(self, state: State):
        return 1

    def decide_best_move_expectimax(self, is_max):
        pass
