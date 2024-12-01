from .simulation_exceptions import SimulationError

class InvalidCarCommandError(SimulationError):
    """Raised when an invalid command is given to a car."""
    def __init__(self, command, message="Invalid command for the car."):
        self.command = command
        super().__init__(f"{message} Command: {command}")

class CarCollisionError(SimulationError):
    """Raised when two cars collide."""
    def __init__(self, car1, car2, position, message="Collision detected."):
        self.car1 = car1
        self.car2 = car2
        self.position = position
        super().__init__(f"{message} {car1} and {car2} collided at {position}.")
