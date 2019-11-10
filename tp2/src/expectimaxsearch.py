import math
from enum import Enum

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.state import State

DONT_CARE = 0


class Agent(Enum):
    MAX = 1
    EXP = 2


def get_next_agent_generator():
    while True:
        yield Agent.MAX
        yield Agent.EXP


class ExpectimaxSearch(MiniMaxSearch):
    def __init__(self, *arg, **kwargs):
        self.agent = get_next_agent_generator()
        super().__init__(*arg, **kwargs)

    def solve_single_player(self, verbose=True) -> State:
        """
        return the nb of steps
        print the state if verbose
        """
        _, final_state = self.get_value(self.rushhour.state)
        if verbose:
            pass
        return final_state.nb_moves

    def get_value(self, state) -> (int, State):
        if state.success():
            return DONT_CARE, state

        agent = next(self.agent)
        if agent == Agent.MAX:
            return self.get_max_value(state)
        elif agent == Agent.EXP:
            return self.get_exp_value(state)

    def get_max_value(self, state: State) -> (int, State):
        child_states = self.rushhour.get_possible_moves(state=state)
        v = math.inf
        best_state = child_states[0]
        for successor_state in child_states:
            local_v, local_state = self.get_value(successor_state)
            if local_v > v:
                v = local_v
                best_state = successor_state

        return v, best_state

    def get_exp_value(self, state: State) -> (int, State):
        child_states = self.rushhour.get_possible_moves(state=state)
        # TODO : UNMOCK
        return 1, child_states[0]

    def decide_best_move_expectimax(self, is_max):
        pass
