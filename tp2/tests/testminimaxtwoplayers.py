import unittest
from time import time

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State
from tp2.tests.table_maker import TableMaker
from .data import *


class TestPruning(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.table_maker = TableMaker(file_name='minimax_result.csv', header=['test_name', 'time (ms)'])

    def execute_minimax_two_players(self, test_name):
        rush_hour: RushHour = RushHour(*self.rush_hour_data)
        rush_hour.state = State(self.state_data)
        algo = MiniMaxSearch(rush_hour, rush_hour.state, 3)
        algo.rushhour.update_free_pos()
        start = time()
        algo.solve_two_players(verbose=False)
        duration = (time() - start) * 1000
        self.table_maker.append_row([test_name, f'{duration:.2f}'])
        print(rush_hour.state.nb_moves)

    def test_solve_two_player_1(self):
        """
        best outcome = 9 moves
        """
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_minimax_two_players(unittest.TestCase.id(self).split('.')[-1])

    def test_solve_two_player_2(self):
        """
        best outcome = 16 moves
        """
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_minimax_two_players(unittest.TestCase.id(self).split('.')[-1])

    def test_solve_two_player_3(self):
        """
        best outcome = 14 moves
        """
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_minimax_two_players(unittest.TestCase.id(self).split('.')[-1])


if __name__ == '__main__':
    unittest.main()
