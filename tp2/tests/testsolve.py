from unittest import TestCase

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State

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


class TestSolve(TestCase):
    def execute_minimax(self):
        rush_hour: RushHour = RushHour(*self.rush_hour_data)
        rush_hour.state = State(self.state_data)
        algo = MiniMaxSearch(rush_hour, rush_hour.state, 1)
        algo.rushhour.update_free_pos()
        algo.solve_1()
        print(rush_hour.state.nb_moves)

    def test_solve_one_player_1(self):
        """
        best outcome = 9 moves
        """
        self.rush_hour_data = rush_hour_data_1
        self.state_data = state_data_1
        self.execute_minimax()
