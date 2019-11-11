import unittest
from time import time

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State
from tp2.tests.table_maker import TableMaker
from .data import *


class TestExpectimax(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.table_maker = TableMaker(file_name='expectimax.csv', header=['test_name', 'time (ms)', 'coups'])

    def execute_expectimax(self, test_name, is_pessimistic=False, is_optimistic=False):
        rush_hour: RushHour = RushHour(*self.rush_hour_data)
        rush_hour.state = State(self.state_data)
        algo = MiniMaxSearch(rush_hour, rush_hour.state, 3)
        algo.rushhour.update_free_pos()
        start = time()
        algo.solve_expectimax(verbose=False, is_pessimistic=is_pessimistic, is_optimistic=is_optimistic)
        duration = (time() - start) * 1000
        self.table_maker.append_row([test_name, f'{duration:.2f}', rush_hour.state.nb_moves])
        print(rush_hour.state.nb_moves)


    def test_expectimax_1(self):
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1])

    def test_expectimax_2(self):
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1])

    def test_expectimax_3(self):
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1])

    def test_expectimax_pessimistic_1(self):
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_pessimistic=True)

    def test_expectimax_pessimistic_2(self):
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_pessimistic=True)

    def test_expectimax_pessimistic_3(self):
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_pessimistic=True)

    def test_expectimax_optimistic_1(self):
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_optimistic=True)

    def test_expectimax_optimistic_2(self):
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_optimistic=True)

    def test_expectimax_optimistic_3(self):
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_expectimax(unittest.TestCase.id(self).split('.')[-1], is_optimistic=True)


if __name__ == '__main__':
    unittest.main()
