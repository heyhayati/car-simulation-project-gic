from simulation.constants import DIRECTIONS

from exceptions.car_exceptions import InvalidCarCommandError

class Car:
    def __init__(self, name: str, x: int, y: int, direction: str):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []
        self.active = True  # Indicates if the car is still processing commands

    def turn_left(self):
        """Rotate 90 degrees counterclockwise."""
        current_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_idx - 1) % 4]

    def turn_right(self):
        """Rotate 90 degrees clockwise."""
        current_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, field_width: int, field_height: int):
        """Move one step forward in the current direction."""
        old_position = (self.x, self.y)
        if self.direction == "N" and self.y < field_height - 1:
            self.y += 1
        elif self.direction == "E" and self.x < field_width - 1:
            self.x += 1
        elif self.direction == "S" and self.y > 0:
            self.y -= 1
        elif self.direction == "W" and self.x > 0:
            self.x -= 1

    def execute_command(self, command: str, field_width: int, field_height: int):
        """Execute a single command."""
        if command == "L":
            self.turn_left()
        elif command == "R":
            self.turn_right()
        elif command == "F":
            self.move_forward(field_width, field_height)
        else:
            raise ValueError(f"Invalid command: {command}")

    def __str__(self):
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"