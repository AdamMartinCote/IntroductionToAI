from unittest import TestCase

from tp2.src.rushhour import RushHour

rush_hour_data_1 = [[True, False, False, False, True],
                    [2, 3, 2, 3, 3],
                    [2, 4, 5, 1, 5],
                    ["rouge", "vert", "bleu", "orange", "jaune"]]

state_data_1 = [1, 0, 1, 3, 2]


class TestSolve(TestCase):
    def test_solve_1(self):
        rush_hour = RushHour(*rush_hour_data_1)
        rush_hour.state = state_data_1
