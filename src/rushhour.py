from collections import deque
from typing import List

import numpy as np
import heapq

from src.state import State


class Car:
    def __init__(self, is_horizontal: bool, length: int, move_on_index: int):
        self.is_horizontal = is_horizontal
        self.length = length
        self.move_on_index = move_on_index


class Rushhour:

    def __init__(self, horiz: List[bool], lengths, move_on, color=None):
        self.nbcars = len(horiz)
        self.cars = []
        for orientation, length, move_on_index in zip(horiz, lengths, move_on):
            self.cars.append(Car(orientation, length, move_on_index))

        self.color = color

        self.free_pos = None

    def init_positions(self, state: State):
        self.free_pos = np.ones((6, 6), dtype=bool)
        for car, p in zip(self.cars, state.pos):
            relative_pos = car.move_on_index
            for i in range(car.length):
                if car.is_horizontal:
                    self.free_pos[relative_pos][i + p] -= 1
                else:
                    self.free_pos[i + p][relative_pos] -= 1

    def possible_moves(self, state):
        self.init_positions(state)
        new_states = []
        # TODO
        return new_states

    def solve(self, state):
        visited = set()
        fifo = deque([state])
        visited.add(state)
        # TODO

        return None

    def solve_Astar(self, state):
        visited = set()
        visited.add(state)

        priority_queue = []
        state.h = state.estimee1()
        heapq.heappush(priority_queue, state)

        # TODO
        return None

    def print_solution(self, state):
        # TODO
        return 0
