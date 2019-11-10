import math
from enum import Enum
from typing import List

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.state import State

DONT_CARE = 0


class Agent(Enum):
    MAX = 1
    EXP = 2


def get_next_agent_generator():
    while True:
        yield Agent.MAX
        # yield Agent.EXP


class ExpectimaxSearch(MiniMaxSearch):
    def __init__(self, *arg, **kwargs):
        self.agent = get_next_agent_generator()
        self.state_history: List[State] = []
        super().__init__(*arg, **kwargs)

    def solve_single_player(self, verbose=True) -> State:
        """
        return the nb of steps
        print the state if verbose
        """

        state = None
        while state is None or not state.success():
            _, state = self.get_value(self.rushhour.state, depth=1)

        if verbose:
            self.rushhour.print_grid()
        return state.nb_moves

    def get_value(self, state, depth=1) -> (int, State):
        if state.success() or depth == 0:
            self.rushhour.state = state
            self.rushhour.update_free_pos()
            self.rushhour.plot_free_pos()
            return self.get_state_utility(state), state

        agent = next(self.agent)
        if agent == Agent.MAX:
            return self.get_max_value(state, depth - 1)
        elif agent == Agent.EXP:
            # TODO : UNMOCK
            return self.get_exp_value(state, depth - 1)

    def get_max_value(self, state: State, depth) -> (int, State):
        child_states = self.rushhour.get_possible_moves(state=state)
        v = math.inf
        best_state = child_states[0]
        for successor_state in child_states:
            local_v, local_state = self.get_value(successor_state, depth)
            if local_v > v:
                v = local_v
                best_state = successor_state

        return v, best_state

    def get_exp_value(self, state: State, depth) -> (int, State):
        child_states = self.rushhour.get_possible_moves(state=state)
        v = 0
        for successor in child_states:
            p = ExpectimaxSearch.probability(successor)
            v += p * self.get_value(successor, depth - 1)[0]
        # TODO : UNMOCK
        return v, child_states[0]

    def get_state_utility(self, state):
        return state.score_heuristic_1(self.visited,
                                       self.rushhour.free_pos,
                                       self.rushhour.length,
                                       self.rushhour.move_on,
                                       self.rushhour.horiz)

    @staticmethod
    def probability(state: State):
        # TODO : UNMOCK
        return 1
