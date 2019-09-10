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


class TestSolve(TestCase):
    def test_solve16(self):
        rh = Rushhour(*game1)
        s = State([1, 0, 1, 4, 2, 4, 0, 1])
        s = rh.solve(s)
        rh.print_solution(s)
        print("\n--------------------------------------------\n")

    def test_solve16_Astar(self):
        rh = Rushhour(*game1)
        s = State([1, 0, 1, 4, 2, 4, 0, 1])
        s = rh.solve_Astar(s)
        rh.print_solution(s)
        print("\n--------------------------------------------\n")

    def test_solve81(self):
        rh = Rushhour(*game2)
        s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        s = rh.solve(s)
        rh.print_solution(s)
        print("\n--------------------------------------------\n")

    def test_solve81_Astar(self):
        rh = Rushhour(*game2)
        s = State([3, 0, 1, 0, 1, 1, 1, 0, 3, 4, 4, 0, 3])
        s = rh.solve_Astar(s)
        rh.print_solution(s)
        print("\n--------------------------------------------\n")

    # TODO: Time after both
    # % time
