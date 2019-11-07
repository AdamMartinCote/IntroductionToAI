from unittest import TestCase

from tp2.src.minmaxsearch import MiniMaxSearch
from tp2.src.rushhour import RushHour
from tp2.src.state import State


class TestUtils(TestCase):

    def test_print_move(self):
        rh = RushHour([True], [2], [2], ["rouge"])
        s = State([0])
        s = s.put_rock((3, 1))  # Roche dans la case 3-1
        s = s.move(0, 1)  # Voiture rouge vers la droite

        algo = MiniMaxSearch(rh, s, 1)
        algo.print_move(True, s)
        algo.print_move(False, s)
