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

    def solve_single_player(self, verbose=True):
        self.get_expectimax_value(self.rushhour.state)

    def execute_expectimax(self, current_depth, current_state, is_max):
        best_move = None
        return best_move

    def get_next_agent_generator(self):
        while True:
            yield Agent.MAX
            yield Agent.EXP

    def get_expectimax_value(self, state):
        if state.success():
            return self.mesure_state_utility(state)

        if next(self.agent) == Agent.MAX:
            return self.get_max_value(state)
        elif next(self.agent) == Agent.EXP:
            return self.get_exp_value(state)

    def get_max_value(self, state: State):
        childs_states = self.rushhour.get_possible_moves()
        v = math.inf
        for successor_state in childs_states:
            v = max(v,
                    self.get_value(successor_state))
        return v

    def get_value(self, state):
        return 1

    def get_exp_value(self, state: State):
        return 1

    def mesure_state_utility(self, state: State):
        return 1

    def decide_best_move_expectimax(self, is_max):
        pass
