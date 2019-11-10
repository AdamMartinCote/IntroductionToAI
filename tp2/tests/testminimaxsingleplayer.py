from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State

from .data import *
from .testbase import TestBase


class TestMinimaxSinglePlayer(TestBase):
    def execute_minimax_single_player(self):
        rush_hour: RushHour = RushHour(*self.rush_hour_data)
        rush_hour.state = State(self.state_data)
        algo = MiniMaxSearch(rush_hour, rush_hour.state, 1)
        algo.rushhour.update_free_pos()
        algo.solve_single_player(verbose=False)
        print(rush_hour.state.nb_moves)

    def test_solve_one_player_1(self):
        """
        best outcome = 9 moves
        """
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_minimax_single_player()

    def test_solve_one_player_2(self):
        """
        best outcome = 16 moves
        """
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_minimax_single_player()

    def test_solve_one_player_3(self):
        """
        best outcome = 14 moves
        """
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_minimax_single_player()
