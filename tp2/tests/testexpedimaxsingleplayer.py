from tp2.src.expectimaxsearch import ExpectimaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State

from .data import *
from .testbase import TestBase
from .testrushhour import TestRushHour
from ..src.heuristics import Heuristics


class TestExpedimaxSinglePlayer(TestBase):
    def test_solve_expectimax(self):
        """
        best outcome = 9 moves
        """
        rush_hour = RushHour(*rush_hour_data_1)
        rush_hour.state = State(state_data_1)
        algo = ExpectimaxSearch(rush_hour, rush_hour.state, 3)
        nb_moves = self.execute_algo_single_player(algo)
        print(nb_moves)
        self.assertEqual(9, nb_moves)

    def test_state_order_sanity(self):
        """
        validate state history make sense
        """
        rush_hour = RushHour(*rush_hour_data_1)
        rush_hour.state = State(state_data_1)
        algo = ExpectimaxSearch(rush_hour, rush_hour.state, 3)
        try:
            self.execute_algo_single_player(algo)
        except Exception:
            pass

        state_history = algo.state_history
        for i, in range(len(state_history) - 1):
            pair = (state_history[i],
                    state_history[i + 1])
            self.assertTrue(TestRushHour.states_are_consecutives(pair[0],
                                                                 pair[1]))

    def test_blocking_heuristics(self):
        heuristics = Heuristics(RushHour(*rush_hour_data_1))
        nb = heuristics.blocking(State(state_data_1))
        self.assertEqual(2, nb)

        # heuristics = Heuristics(RushHour(*rush_hour_data_2))
        # nb = heuristics.blocking(State(state_data_2))
        # self.assertEqual(2, nb)

        heuristics = Heuristics(RushHour(*rush_hour_data_3))
        nb = heuristics.blocking(State(state_data_3))
        self.assertEqual(3, nb)
