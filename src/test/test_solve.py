import time
import unittest
from unittest import TestCase

from src.rushhour import Rushhour
from src.state import State

game1 = [[True, True, False, False, True, True, False, False],
         [2, 2, 3, 2, 3, 2, 3, 3],
         [2, 0, 0, 0, 5, 4, 5, 3],
         ["rouge", "vert clair", "violet", "orange", "vert", "bleu ciel", "jaune", "bleu"]]

game2 = [[True, False, True, False, False, False, False, True, False, False, True, True, True],
         [2, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2],
         [2, 0, 0, 4, 1, 2, 5, 3, 3, 2, 4, 5, 5],
         ["rouge", "jaune", "vert clair", "orange", "bleu clair", "rose", "violet clair", "bleu", "violet",
          "vert", "noir", "beige", "jaune clair"]]

game3 = [[True, False, True, False, False, True, False, True, False, True, False, True],
         [2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 3],
         [2, 2, 0, 0, 3, 1, 1, 3, 0, 4, 5, 5],
         ["rouge", "vert clair", "jaune", "orange", "violet clair", "bleu ciel", "rose", "violet", "vert",
          "noir", "beige", "bleu"]]


class TestSolve(TestCase):

    @staticmethod
    def is_solved(state) -> bool:
        wanted_car_position = 4
        return state.pos[Rushhour.RED_CAR] == wanted_car_position

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime

        print("\n--------------------------------------------")
        print(self._testMethodName)
        print('')
        self.rh.print_solution(self.s)
        print('')
        print("%s: %.3fs" % (self.id(), t))
        print(f'nb visited = {self.visited}')
        # print("\n--------------------------------------------")

    def test_solve46(self):
        self.rh = Rushhour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.s, self.visited = self.rh.solve(self.s)
        self.assertTrue(TestSolve.is_solved(self.s))
        self.assertEqual(self.s.nb_moves, 46)

    def test_solve46_Astar(self):
        self.rh = Rushhour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.s, self.visited = self.rh.solve_Astar(self.s)
        self.assertTrue(TestSolve.is_solved(self.s))
        self.assertEqual(self.s.nb_moves, 46)

    def test_solve16(self):
        self.rh = Rushhour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.s, self.visited = self.rh.solve(self.s)
        self.assertEqual(TestSolve.is_solved(self.s), True)
        self.assertEqual(self.s.nb_moves, 16)

    # @unittest.skip("not implemented")
    def test_solve16_Astar(self):
        self.rh = Rushhour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.s, self.visited = self.rh.solve_Astar(self.s)
        self.assertEqual(TestSolve.is_solved(self.s), True)
        self.assertEqual(self.s.nb_moves, 16)

    def test_solve81(self):
        self.rh = Rushhour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.s, self.visited = self.rh.solve(self.s)
        self.assertEqual(TestSolve.is_solved(self.s), True)
        self.assertEqual(self.s.nb_moves, 81)

    # @unittest.skip("not implemented")
    def test_solve81_Astar(self):
        self.rh = Rushhour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.s, self.visited = self.rh.solve_Astar(self.s)
        self.assertEqual(TestSolve.is_solved(self.s), True)
        self.assertEqual(self.s.nb_moves, 81)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolve)
    unittest.TextTestRunner(verbosity=0).run(suite)
