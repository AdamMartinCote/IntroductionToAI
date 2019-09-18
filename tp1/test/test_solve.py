import time
import unittest
from unittest import TestCase

from tp1.src.rushhour import RushHour
from tp1.src.state import State
from tp1.test.common import print_header

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
        return state.pos[RushHour.RED_CAR] == wanted_car_position

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print_header(self._testMethodName)

        print('')
        self.rh.print_solution(self.s)
        print('')
        print(f'elapsed\t\t:\t%.3fs' % t)
        print(f'nb visited\t:\t{self.visited}')

    def do_test(self):
        self.algo = getattr(self.rh, self.algo_name)
        self.s, self.visited = self.algo(self.s)
        self.assertTrue(TestSolve.is_solved(self.s))
        self.assertEqual(self.s.nb_moves, self.expected_nb_step)

    def test_solve46(self):
        self.rh = RushHour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.algo_name = 'solve'
        self.expected_nb_step = 46
        self.do_test()

    def test_solve16(self):
        self.rh = RushHour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.algo_name = 'solve'
        self.expected_nb_step = 16
        self.do_test()

    def test_solve81(self):
        self.rh = RushHour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.algo_name = 'solve'
        self.expected_nb_step = 81
        self.do_test()

    def test_solve46_Astar(self):
        self.rh = RushHour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.algo_name = 'solve_Astar'
        self.expected_nb_step = 46
        self.do_test()

    def test_solve16_Astar(self):
        self.rh = RushHour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.algo_name = 'solve_Astar'
        self.expected_nb_step = 16
        self.do_test()

    def test_solve81_Astar(self):
        self.rh = RushHour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.algo_name = 'solve_Astar'
        self.expected_nb_step = 81
        self.do_test()

    def test_solve46_Astar_prime(self):
        self.rh = RushHour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.algo_name = 'solve_Astar_prime'
        self.expected_nb_step = 46
        self.do_test()

    def test_solve16_Astar_prime(self):
        self.rh = RushHour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.algo_name = 'solve_Astar_prime'
        self.expected_nb_step = 16
        self.do_test()

    def test_solve81_Astar_prime(self):
        self.rh = RushHour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.algo_name = 'solve_Astar_prime'
        self.expected_nb_step = 81
        self.do_test()

    def test_solve46_Astar_prime_prime(self):
        self.rh = RushHour(*game3)
        self.s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.algo_name = 'solve_Astar_prime_prime'
        self.expected_nb_step = 46
        self.do_test()

    def test_solve16_Astar_prime_prime(self):
        self.rh = RushHour(*game1)
        self.s = State([1, 0, 1, 4, 2, 4, 0, 1])
        self.algo_name = 'solve_Astar_prime_prime'
        self.expected_nb_step = 16
        self.do_test()

    def test_solve81_Astar_prime_prime(self):
        self.rh = RushHour(*game2)
        self.s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        self.algo_name = 'solve_Astar_prime_prime'
        self.expected_nb_step = 81
        self.do_test()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolve)
    unittest.TextTestRunner(verbosity=0).run(suite)
