import heapq
from collections import deque
from typing import List

import numpy as np

from src.state import State


class Car:
    def __init__(self, is_horizontal: bool, length: int, move_on_index: int):
        self.is_horizontal = is_horizontal
        self.is_vertical = not is_horizontal
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
        """ true means empty... :/
        """
        self.free_pos = np.ones((6, 6), dtype=bool)
        for car, p in zip(self.cars, state.pos):
            relative_pos = car.move_on_index
            for i in range(car.length):
                if car.is_horizontal:
                    self.free_pos[relative_pos][i + p] -= 1
                else:
                    self.free_pos[i + p][relative_pos] -= 1

    def possible_moves(self, state) -> List[State]:
        def check_if_position_empty_and_valid(position):
            is_inbound = 0 <= position[0] < 6 and 0 <= position[1] < 6
            return is_inbound and self.free_pos[position[0]][position[1]]

        self.init_positions(state)
        new_states: List[State] = []
        for i, car_and_p in enumerate(zip(self.cars, state.pos)):
            car = car_and_p[0]
            p = car_and_p[1]

            space_in_font = (car.move_on_index, p + car.length) if car.is_horizontal \
                else (p + car.length, car.move_on_index)
            space_in_rear = (car.move_on_index, p - 1) if car.is_horizontal \
                else (p - 1, car.move_on_index)
            if check_if_position_empty_and_valid(space_in_font):
                new_states.append(state.move(i, 1))
            if check_if_position_empty_and_valid(space_in_rear):
                new_states.append(state.move(i, -1))

        return new_states

    def solve(self, state) -> State or None:
        """
        Create a breadth-first graph of all possible
        append and popLeft
        """
        visited = set()
        fifo = deque([state])

        while len(fifo) > 0:
            # print(len(fifo))
            to_evaluate: State = fifo.popleft()
            if to_evaluate in visited:
                continue
            visited.add(to_evaluate)
            if to_evaluate.success():
                # print('got it bitches')
                return to_evaluate
            else:
                children: List[State] = self.possible_moves(to_evaluate)
                fifo.extend(filter(lambda x: x not in visited, children))

        return None

    def solve_Astar(self, state):
        visited = set()
        visited.add(state)

        priority_queue = []
        state.h = state.estimee1()
        heapq.heappush(priority_queue, state)

        # TODO
        return None

    def print_solution(self, state: State) -> None:
        self.render(state)

    def render(self, state: State) -> None:
        dim = len(self.free_pos)
        grid = np.zeros((dim, dim), dtype=int)
        red_car = self.cars[0]
        if red_car.is_horizontal:
            for i in range(red_car.length):
                grid[red_car.move_on_index][state.pos[0] + i] = 1
        if red_car.is_vertical:
            for i in range(red_car.length):
                grid[state.pos[0] + i][red_car.move_on_index] = 1

        print(grid)
