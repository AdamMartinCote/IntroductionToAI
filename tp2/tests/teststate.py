import random
from copy import copy
from unittest import TestCase

import numpy as np

from tp2.src.rushhour import RushHour
from tp2.src.state import State


class TestState(TestCase):
    def setUp(self) -> None:
        self.rh = RushHour([True, False, True, False, False, True, False, True, False, True, False, True],
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

        self.rh.state = s0
        self.rh.print_pretty_grid_and_update_free_pos(s0)
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

        np.testing.assert_array_equal(self.rh.get_formatted_grid_and_update_free_pos(s0), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

        print("Roche 4-4")

        self.rh.state = s1
        self.rh.update_free_pos()
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
        np.testing.assert_array_equal(self.rh.get_formatted_grid_and_update_free_pos(s1), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

        print("Roche 3-2")

        self.rh.state = s2
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
             [False, False, False, False, True, False],  # Todo: Demander au chargé multiple rock à (4,4)
             [False, False, False, False, True, False]],
            dtype='bool'
        )
        np.testing.assert_array_equal(self.rh.get_formatted_grid_and_update_free_pos(s2), grid_reference)
        np.testing.assert_array_equal(self.rh.free_pos, free_pos_reference)

    def testPossibleRockMoves(self):
        s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
        self.rh.state = s
        sols = self.rh.possible_rock_moves()
        print(len(sols))
        self.assertEqual(7, len(sols))
        s1 = s.put_rock((3, 4))
        self.rh.state = s1
        sols = self.rh.possible_rock_moves()
        print(len(sols))
        self.assertEqual(3, len(sols))

    def test_hash_function(self):
        s0 = State([random.randint(1, 10) for i in range(12)])
        s1 = State([random.randint(1, 10) for i in range(12)])
        s2 = State([random.randint(1, 10) for i in range(12)])

        s0_copy = copy(s0)
        s1_copy = copy(s1)
        s2_copy = copy(s2)

        self.assertEqual(hash(s0), hash(s0_copy))
        self.assertEqual(hash(s1), hash(s1_copy))
        self.assertEqual(hash(s2), hash(s2_copy))

        self.assertNotEqual(hash(s0), hash(s1))
        self.assertNotEqual(hash(s0), hash(s2))

        self.assertNotEqual(hash(s1), hash(s0))
        self.assertNotEqual(hash(s1), hash(s2))

        self.assertNotEqual(hash(s2), hash(s0))
        self.assertNotEqual(hash(s2), hash(s1))
