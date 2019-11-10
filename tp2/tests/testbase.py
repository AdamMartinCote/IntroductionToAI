from unittest import TestCase


class TestBase(TestCase):
    def execute_algo_single_player(self, algo) -> int:
        algo.rushhour.update_free_pos()
        algo.solve_single_player(verbose=False)
        return algo.rushhour.state.nb_moves
