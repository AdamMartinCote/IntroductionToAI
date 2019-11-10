import numpy as np

from tp2.src.rushhour import RushHour


class Heuristics:
    def __init__(self, rush_hour: RushHour):
        self.rush_hour = rush_hour

    def blocking(self, state) -> int:
        grid: np.ndarray = self.rush_hour.get_formatted_grid_and_update_free_pos(state)
        red_car_line = grid[self.rush_hour.move_on[0]]
        path = red_car_line[state.pos[state.pos[0] + self.rush_hour.length[0]]:]
        nb_blocking = sum([1 if square is not b'-' else 0 for square in path])
        print(red_car_line)
        print(path)
        print(nb_blocking)
        return nb_blocking
