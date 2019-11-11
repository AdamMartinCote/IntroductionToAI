import numpy as np

from tp2.src.rushhour import RushHour


class Heuristics:
    def __init__(self, rush_hour: RushHour):
        self.rush_hour = rush_hour

    def blocking(self, state) -> int:
        grid: np.ndarray = self.rush_hour.get_formatted_grid_and_update_free_pos(state)
        red_car_line = grid[self.rush_hour.move_on[0]]
        path = []
        for idx in range(len(red_car_line) - 1, -1, -1):
            if red_car_line[idx] == b'r':
                break
            else:
                path.append(red_car_line[idx])

        nb_blocking = sum([1 if square is not b'-' else 0 for square in path])
        # print(red_car_line)
        # print(path)
        # print(nb_blocking)
        return -nb_blocking
