from unittest import TestCase

from .data import *
from ..src.rushhour import RushHour
from ..src.state import State


class TestRushHour(TestCase):
    def test_get_possible_moves(self):
        self.rushHour = RushHour(*rush_hour_data_1)
        self.rushHour.state = State(state_data_1)

        current_state = self.rushHour.state
        possible_moves = self.rushHour.get_possible_moves()
        for possible_state in possible_moves:
            self.assertTrue(TestRushHour.states_are_consecutives(current_state, possible_state))

        self.rushHour = RushHour(*rush_hour_data_2)
        self.rushHour.state = State(state_data_2)

        current_state = self.rushHour.state
        possible_moves = self.rushHour.get_possible_moves()
        for possible_state in possible_moves:
            self.assertTrue(TestRushHour.states_are_consecutives(current_state, possible_state))

        self.rushHour = RushHour(*rush_hour_data_3)
        self.rushHour.state = State(state_data_3)

        current_state = self.rushHour.state
        possible_moves = self.rushHour.get_possible_moves()
        for possible_state in possible_moves:
            self.assertTrue(TestRushHour.states_are_consecutives(current_state, possible_state))

    @staticmethod
    def states_are_consecutives(a: State, b: State) -> bool:
        """
        return true if it is possible to get from a to b in one move
        """
        nb_changes = 0
        for pos_a, pos_b in zip(a.pos, b.pos):
            if pos_a != pos_b:
                nb_changes += 1
        return nb_changes == 1
