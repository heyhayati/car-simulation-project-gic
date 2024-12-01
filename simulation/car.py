# car.py
from constants import DIRECTIONS

class Car:
    def __init__(self, name: str, x: int, y: int, direction: str):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []
        self.active = True

    def turn_left(self):
        """Turn the car 90 degrees to the left."""
        current_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_idx - 1) % 4]

    def turn_right(self):
        """Turn the car 90 degrees to the right."""
        current_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, field_width: int, field_height: int):
        """Move the car forward by one grid point."""
        if not self.active:
            return
        if self.direction == 'N' and self.y < field_height - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < field_width - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def execute_command(self, command: str, field_width: int, field_height: int):
        """Execute a single command."""
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'F':
            self.move_forward(field_width, field_height)

    def __str__(self):
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"
