import unittest
from time import time

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State
from tp2.tests.table_maker import TableMaker

rush_hour_data_1 = [[True, False, False, False, True],
                    [2, 3, 2, 3, 3],
                    [2, 4, 5, 1, 5],
                    ["rouge", "vert", "bleu", "orange", "jaune"]]

rush_hour_data_2 = [[True, True, False, False, True, True, False, False],
                    [2, 2, 3, 2, 3, 2, 3, 3],
                    [2, 0, 0, 0, 5, 4, 5, 3],
                    ["rouge", "vert", "mauve", "orange", "emeraude", "lime", "jaune", "bleu"]]

rush_hour_data_3 = [[True, False, True, False, False, False, True, True, False, True, True],
                    [2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2],
                    [2, 0, 0, 3, 4, 5, 3, 5, 2, 5, 4],
                    ["rouge", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]

state_data_1 = [1, 0, 1, 3, 2]
state_data_2 = [1, 0, 1, 4, 2, 4, 0, 1]
state_data_3 = [0, 0, 3, 1, 2, 1, 0, 0, 4, 3, 4]


class TestPruning(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.table_maker = TableMaker(file_name='pruning_result.csv', header=['test_name', 'time (ms)'])

    def execute_pruning(self, test_name):
        rush_hour: RushHour = RushHour(*self.rush_hour_data)
        rush_hour.state = State(self.state_data)
        algo = MiniMaxSearch(rush_hour, rush_hour.state, 3)
        algo.rushhour.update_free_pos()
        start = time()
        algo.solve_pruning(verbose=False)
        duration = (time() - start) * 1000
        self.table_maker.append_row([test_name, f'{duration:.2f}'])
        print(rush_hour.state.nb_moves)


    def test_pruning_1(self):
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_pruning(unittest.TestCase.id(self).split('.')[-1])

    def test_pruning_2(self):
        self.rush_hour_data = rush_hour_data_2
        self.state_data = state_data_2
        self.execute_pruning(unittest.TestCase.id(self).split('.')[-1])

    def test_pruning_3(self):
        self.rush_hour_data = rush_hour_data_3
        self.state_data = state_data_3
        self.execute_pruning(unittest.TestCase.id(self).split('.')[-1])


if __name__ == '__main__':
    unittest.main()
