import math
from enum import Enum

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.state import State


class Agent(Enum):
    MAX = 1
    EXP = 2


class ExpectimaxSearch(MiniMaxSearch):
    def __init__(self, *arg, **kwargs):
        self.agent = self.get_next_agent_generator()
        super().__init__(*arg, **kwargs)

    def solve_single_player(self, verbose=True) -> State:
        """
        return the final state once solved
        print the state if verbose
        """
        final_state = self.get_expectimax_value(self.rushhour.state)
        if verbose:
            pass
        return final_state

    def execute_expectimax(self, current_depth, current_state, is_max):
        best_move = None
        return best_move

    def get_next_agent_generator(self):
        while True:
            yield Agent.MAX
            yield Agent.EXP

    def get_expectimax_value(self, state) -> State:
        if state.success():
            return state

        if next(self.agent) == Agent.MAX:
            return self.get_max_value(state)
        elif next(self.agent) == Agent.EXP:
            return self.get_exp_value(state)

    def get_max_value(self, state: State) -> State:
        childs_states = self.rushhour.get_possible_moves()
        v = math.inf
        best_state = childs_states[0]
        for successor_state in childs_states:
            local_v = self.get_expectimax_value(successor_state)
            if local_v > v:
                v = local_v
                best_state = successor_state

        return best_state

    def get_value(self, state):
        return 1

    def get_exp_value(self, state: State):
        return 1

    def mesure_state_utility(self, state: State):
        return 1

    def decide_best_move_expectimax(self, is_max):
        pass
