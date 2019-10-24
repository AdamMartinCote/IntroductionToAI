from unittest import TestCase

import numpy as np

from tp2.src.rushhour import Rushhour
from tp2.src.state import State


class TestState(TestCase):
    def setUp(self) -> None:
        self.rh = Rushhour([True, False, True, False, False, True, False, True, False, True, False, True],
                           [2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 3],
                           [2, 2, 0, 0, 3, 1, 1, 3, 0, 4, 5, 5],
                           ["rouge", "vert clair", "jaune", "orange", "violet clair", "bleu ciel", "rose", "violet",
                            "vert",
                            "noir", "beige", "bleu"])

    def testRocks(self):
        s0 = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        s1 = s0.put_rock((4, 4))
        s2 = s1.put_rock((3, 2))

        print("État initial")
        self.rh.print_pretty_grid(s0)
        print(self.rh.free_pos)
        print('\n')
        grid_reference = np.array(
            [['-', '-', 'v', 'j', 'j', 'j'],
             ['o', '-', 'v', 'v', 'b', 'b'],
             ['o', 'r', 'r', 'v', '-', '-'],
             ['-', 'r', '-', 'v', 'v', 'v'],
             ['v', 'r', 'n', 'n', '-', 'b'],
             ['v', 'b', 'b', 'b', '-', 'b']],
            dtype='|S1'
        )
        free_pos_reference = np.array(
            [[True, True, False, False, False, False],
             [False, True, False, False, False, False],
             [False, False, False, False, True, True],
             [True, False, True, False, False, False],
             [False, False, False, False, True, False],
             [False, False, False, False, True, False]],
            dtype='bool'
        )

        np.testing.assert_array_equal(self.rh.get_formatted_grid(s0), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

        print("Roche 4-4")
        self.rh.print_pretty_grid(s1)
        print(self.rh.free_pos)
        print('\n')
        grid_reference = np.array(
            [[b'-', b'-', b'v', b'j', b'j', b'j'],
             [b'o', b'-', b'v', b'v', b'b', b'b'],
             [b'o', b'r', b'r', b'v', b'-', b'-'],
             [b'-', b'r', b'-', b'v', b'v', b'v'],
             [b'v', b'r', b'n', b'n', b'x', b'b'],
             [b'v', b'b', b'b', b'b', b'-', b'b']],
            dtype='|S1'
        )
        free_pos_reference = np.array(
            [[True, True, False, False, False, False],
             [False, True, False, False, False, False],
             [False, False, False, False, True, True],
             [True, False, True, False, False, False],
             [False, False, False, False, False, False],
             [False, False, False, False, True, False]],
            dtype='bool'
        )
        np.testing.assert_array_equal(self.rh.get_formatted_grid(s0), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

        print("Roche 3-2")
        self.rh.print_pretty_grid(s2)
        print(self.rh.free_pos)
        print('\n')
        grid_reference = np.array(
            [[b'-', b'-', b'v', b'j', b'j', b'j'],
             [b'o', b'-', b'v', b'v', b'b', b'b'],
             [b'o', b'r', b'r', b'v', b'-', b'-'],
             [b'-', b'r', b'x', b'v', b'v', b'v'],
             [b'v', b'r', b'n', b'n', b'-', b'b'],
             [b'v', b'b', b'b', b'b', b'-', b'b']],
            dtype='|S1'
        )
        free_pos_reference = np.array(
            [[True, True, False, False, False, False],
             [False, True, False, False, False, False],
             [False, False, False, False, True, True],
             [True, False, False, False, False, False],
             [False, False, False, False, False, False],
             [False, False, False, False, True, False]],
            dtype='bool'
        )
        np.testing.assert_array_equal(self.rh.get_formatted_grid(s0), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

    def testPossibleRockMoves(self):
        s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        sols = self.rh.possible_rock_moves(s)
        print(len(sols))
        s1 = s.put_rock((3, 4))
        sols = self.rh.possible_rock_moves(s1)
        print(len(sols))
