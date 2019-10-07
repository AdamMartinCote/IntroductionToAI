import heapq
from collections import deque
from typing import List

import numpy as np

from tp1.src.car import Car
from tp1.src.state import State


class RushHour:
    RED_CAR = 0

    def __init__(self, horiz: List[bool], lengths, move_on, color=None):
        self.nb_cars = len(horiz)
        self.cars = []
        for orientation, length, move_on_index in zip(horiz, lengths, move_on):
            self.cars.append(Car(orientation, length, move_on_index))

        self.color = color

        self.free_pos = None

    @staticmethod
    def get_free_pos(state: State, cars) -> np.ndarray:
        """ true means empty... :/
        """
        fp = np.ones((6, 6), dtype=bool)
        for car, p in zip(cars, state.pos):
            relative_pos = car.move_on_index
            for i in range(car.length):
                if car.is_horizontal:
                    fp[relative_pos][i + p] -= 1
                else:
                    fp[i + p][relative_pos] -= 1
        return fp

    def possible_moves(self, state) -> List[State]:
        def check_if_position_empty_and_valid(position):
            is_inbound = 0 <= position[0] < 6 and 0 <= position[1] < 6
            return is_inbound and self.free_pos[position[0]][position[1]]

        self.free_pos = self.get_free_pos(state, self.cars)
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

    def solve(self, state) -> (State or None, int):
        """
        Create a breadth-first graph of all possible
        append and popLeft
        """
        visited = set()
        fifo = deque([state])

        while len(fifo) > 0:
            state_to_evaluate: State = fifo.popleft()
            if state_to_evaluate in visited:
                continue
            visited.add(state_to_evaluate)
            if state_to_evaluate.success():
                return state_to_evaluate, len(visited)
            else:
                children: List[State] = self.possible_moves(state_to_evaluate)
                fifo.extend(filter(lambda x: x not in visited, children))

        return None, len(visited)

    def solve_Astar(self, state: State) -> (State or None, int):
        visited = set()

        priority_queue = []
        state.h = state.estimee1()
        heapq.heappush(priority_queue, state)

        while len(priority_queue) > 0:

            state_to_evaluate: State = heapq.heappop(priority_queue)

            if state_to_evaluate in visited:
                continue
            visited.add(state_to_evaluate)
            if state_to_evaluate.success():
                return state_to_evaluate, len(visited)
            else:
                children: List[State] = self.possible_moves(state_to_evaluate)
                for child in children:
                    if child not in visited:
                        child.h = child.estimee1()
                        heapq.heappush(priority_queue, child)
        return None, len(visited)

    def solve_Astar_prime(self, state: State) -> (State or None, int):
        visited = set()

        priority_queue = []
        self.free_pos = self.get_free_pos(state, self.cars)
        state.h = state.estimee2(self.free_pos, self.cars)
        heapq.heappush(priority_queue, state)

        while len(priority_queue) > 0:
            state_to_evaluate: State = heapq.heappop(priority_queue)

            if state_to_evaluate in visited:
                continue
            visited.add(state_to_evaluate)
            if state_to_evaluate.success():
                return state_to_evaluate, len(visited)
            else:
                children: List[State] = self.possible_moves(state_to_evaluate)
                for child in children:
                    if child not in visited:
                        child.h = child.estimee2(self.free_pos, self.cars)
                        heapq.heappush(priority_queue, child)
        return None, len(visited)

    def solve_Astar_prime_prime(self, state: State) -> (State or None, int):
        visited = set()

        priority_queue = []
        self.free_pos = self.get_free_pos(state, self.cars)
        state.h = state.estimee3(self.free_pos, self.cars)
        heapq.heappush(priority_queue, state)

        while len(priority_queue) > 0:
            state_to_evaluate: State = heapq.heappop(priority_queue)

            if state_to_evaluate in visited:
                continue
            visited.add(state_to_evaluate)
            if state_to_evaluate.success():
                return state_to_evaluate, len(visited)
            else:
                children: List[State] = self.possible_moves(state_to_evaluate)
                for child in children:
                    if child not in visited:
                        child.h = child.estimee3(self.free_pos, self.cars)
                        heapq.heappush(priority_queue, child)
        return None, len(visited)

    def print_solution(self, state: State) -> None:
        self.render(state)

    def render(self, state: State) -> None:
        dim = len(self.free_pos)
        grid = np.zeros((dim, dim), dtype=int)
        for idx, car in enumerate(self.cars):
            if car.is_horizontal:
                for i in range(car.length):
                    grid[car.move_on_index][state.pos[idx] + i] = idx + 1
            if car.is_vertical:
                for i in range(car.length):
                    grid[state.pos[idx] + i][car.move_on_index] = idx + 1

        print(grid)
