class Car:
    def __init__(self, is_horizontal: bool, length: int, move_on_index: int):
        self.is_horizontal = is_horizontal
        self.is_vertical = not is_horizontal
        self.length = length
        self.move_on_index = move_on_index
