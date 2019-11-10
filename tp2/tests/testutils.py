from unittest import TestCase

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State
from .data import *


class TestUtils(TestCase):

    def test_print_move(self):
        rh = RushHour([True], [2], [2], ["rouge"])
        s = State([0])
        s = s.put_rock((3, 1))  # Roche dans la case 3-1
        s = s.move(0, 1)  # Voiture rouge vers la droite

        algo = MiniMaxSearch(rh, s, 1)
        self.assertEqual(algo.str_move(True, s), 'Voiture rouge vers la droite')
        self.assertEqual(algo.str_move(False, s), 'Roche dans la case 3-1')

    def test_print_pretty(self):
        rh = RushHour(*rush_hour_data_1)
        state = State(state_data_1)
        rh.print_pretty_grid_and_update_free_pos(state)
