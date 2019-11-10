from typing import List

import matplotlib.pyplot as plt
import numpy as np

from tp2.src.state import State

FREE = True
OCCUPIED = False


class RushHour:

    def __init__(self, horiz, length, move_on, color=None, initial_state=None):
        self.nbcars = len(horiz)
        self.horiz = horiz
        self.length = length
        self.move_on = move_on
        self.color = color

        self.free_pos = None
        self.state = initial_state

    def update_free_pos(self) -> None:
        if not self.state:
            return
        self.free_pos = np.ones((6, 6), dtype=bool)
        for i in range(self.nbcars):
            if self.horiz[i]:
                self.free_pos[self.move_on[i], self.state.pos[i]:self.state.pos[i] + self.length[i]] = OCCUPIED
            else:
                self.free_pos[self.state.pos[i]:self.state.pos[i] + self.length[i], self.move_on[i]] = OCCUPIED

        if self.state.rock:
            self.free_pos[self.state.rock[0]][self.state.rock[1]] = OCCUPIED

    def get_possible_moves(self, state=None) -> List[State]:
        if state is None:
            state = self.state
        self.update_free_pos()
        new_states = []
        for i in range(self.nbcars):
            if self.horiz[i]:
                if state.pos[i] + self.length[i] - 1 < 5 and self.free_pos[self.move_on[i],
                                                                           state.pos[i] + self.length[i]]:
                    new_states.append(state.move(i, +1))
                if state.pos[i] > 0 and self.free_pos[self.move_on[i], state.pos[i] - 1]:
                    new_states.append(state.move(i, -1))
            else:
                if state.pos[i] + self.length[i] - 1 < 5 and self.free_pos[state.pos[i] + self.length[i],
                                                                           self.move_on[i]]:
                    new_states.append(state.move(i, +1))
                if state.pos[i] > 0 and self.free_pos[state.pos[i] - 1, self.move_on[i]]:
                    new_states.append(state.move(i, -1))
        return new_states

    def possible_rock_moves(self) -> List[State]:
        self.update_free_pos()
        new_states = []
        line_idx = [i for i in range(6)]
        col_idx = [i for i in range(6)]
        line_idx.remove(2)
        if self.state.rock:
            line_idx.remove(self.state.rock[0])
            col_idx.remove(self.state.rock[1])
        for i in line_idx:
            for j in col_idx:
                if self.free_pos[i][j]:
                    new_states.append(self.state.put_rock((i, j,)))

        return new_states

    def print_pretty_grid_and_update_free_pos(self, state) -> None:
        grid = self.get_formatted_grid_and_update_free_pos(state)
        print(grid)

    def get_formatted_grid_and_update_free_pos(self, state) -> np.ndarray:
        self.update_free_pos()
        grid = np.chararray((6, 6))
        grid[:] = '-'
        for car in range(self.nbcars):
            for pos in range(state.pos[car], state.pos[car] + self.length[car]):
                if self.horiz[car]:
                    grid[self.move_on[car]][pos] = self.color[car][0]
                else:
                    grid[pos][self.move_on[car]] = self.color[car][0]
        if state.rock:
            grid[state.rock] = 'x'
        return grid

    def plot_free_pos(self):
        plt.imshow(self.free_pos)
        plt.show()

    def print_grid(self, state) -> None:
        plt.imshow(self.get_formatted_grid_and_update_free_pos(state))
        plt.show()
