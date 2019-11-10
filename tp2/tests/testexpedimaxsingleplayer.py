from tp2.src.expectimaxsearch import ExpectimaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State

from .data import *
from .testbase import TestBase


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
