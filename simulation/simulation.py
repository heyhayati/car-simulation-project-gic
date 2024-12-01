from simulation.car import Car
from simulation.field import Field

class Simulation:
    def __init__(self):
        self.field = None
        self.cars = []

    def create_field(self, width: int, height: int):
        """Initialize the simulation field."""
        self.field = Field(width, height)
        print(f"Field created with dimensions {width} x {height}.")

    def add_car(self, name: str, x: int, y: int, direction: str, commands: str):
        """Add a new car to the simulation."""
        if not self.field.is_within_bounds(x, y):
            raise ValueError(f"Initial position ({x},{y}) is out of bounds!")
        car = Car(name, x, y, direction)
        car.commands = list(commands)
        self.cars.append(car)
        print(f"Car {car} added.")

    def process_commands(self):
        """Run simulation step by step."""
        active_cars = {car.name: car for car in self.cars}
        step = 0

        while active_cars:
            step += 1
            new_positions = {}

            for car in list(active_cars.values()):
                if car.commands:
                    command = car.commands.pop(0)
                    car.execute_command(command, self.field.width, self.field.height)
                    position = (car.x, car.y)

                    if position in new_positions:
                        print(f"Collision! {car.name} collided with {new_positions[position].name} at {position} on step {step}.")
                        car.active = False
                        new_positions[position].active = False
                        active_cars.pop(car.name, None)
                        active_cars.pop(new_positions[position].name, None)
                    else:
                        new_positions[position] = car

                if not car.commands:
                    active_cars.pop(car.name, None)

    def show_results(self):
        """Display the final positions of all cars."""
        print("\nFinal positions after simulation:")
        for car in self.cars:
            print(car)

    def reset_simulation(self):
        """Reset the simulation to start over."""
        self.field = None
        self.cars = []
