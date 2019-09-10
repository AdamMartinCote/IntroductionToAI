from unittest import TestCase

from TP1.src.rushhour import RushHour
from TP1.src.state import State


class TestRushHour(TestCase):
    def setUp(self) -> None:
        pass

    def test2(self):
        """ move_on describe the position of the car, according to its orientation
        """
        rh = RushHour([True, True, False, False, True, True, False, False],
                      [2, 2, 3, 2, 3, 2, 3, 3],
                      [2, 0, 0, 0, 5, 4, 5, 3])
        s = State([1, 0, 1, 4, 2, 4, 0, 1])
        rh.init_positions(s)
        b = True
        print(rh.free_pos)
        ans = [[False, False, True, True, True, False], [False, True, True, False, True, False],
               [False, False, False, False, True, False],
               [False, True, True, False, True, True], [False, True, True, True, False, False],
               [False, True, False, False, False, True]]
        b = b and (rh.free_pos[i, j] == ans[i, j] for i in range(6) for j in range(6))
        print("\n", "résultat correct" if b else "mauvais résultat")

        self.assertTrue(b)
        
    def test_possibles_moves(self) -> None:
        rh = RushHour([True, False, True, False, False, True, False, True, False, True, False, True],
                      [2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 3],
                      [2, 2, 0, 0, 3, 1, 1, 3, 0, 4, 5, 5])
        s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        s2 = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 2])

        val1 = len(rh.possible_moves(s))
        self.assertEqual(val1, 5)
        print(val1)

        val2 = len(rh.possible_moves(s2))
        self.assertEqual(val1, 5)
        print(val2)
