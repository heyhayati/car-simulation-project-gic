from simulation.car import Car
from simulation.field import Field

class Simulation:
    def __init__(self):
        self.field = None
        self.cars = []

    def create_field(self, width: int, height: int):
        """Create the simulation field."""
        if width <= 0 or height <= 0:
            raise ValueError("Field dimensions must be positive integers.")
        self.field = Field(width, height)

    def add_car(self, name: str, x: int, y: int, direction: str, commands: str):
        """Add a car to the field."""
        # Check if the car name is unique
        if any(car.name == name for car in self.cars):
            raise ValueError(f"Car name '{name}' must be unique.")

        # Validate position
        if not self.field.is_within_bounds(x, y):
            raise ValueError(f"Car {name} position ({x}, {y}) is out of bounds.")

        # Add the car to the simulation
        car = Car(name, x, y, direction)
        car.commands = list(commands)
        self.cars.append(car)

    def get_initial_cars(self):
        """Get the initial list of cars."""
        return "\n".join(
            f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}"
            for car in self.cars
        )

    def process_commands(self):
        """Run simulation step by step, detecting collisions."""
        if not self.cars:
            print("No cars to simulate.")
            return []

        collision_details = []  # Store details of collisions
        step = 0

        while any(car.commands for car in self.cars):
            step += 1
            positions = {}  # Track positions of cars during this step

            print(f"\nStep {step}:")
            for car in self.cars:
                if car.commands and car.active:  # Ensure the car is active
                    command = car.commands.pop(0)
                    print(f"Car {car.name} executing command {command}")
                    car.execute_command(command, self.field.width, self.field.height)
                    print(f"Car {car.name} moved to ({car.x}, {car.y})")

                    # Detect collisions
                    new_position = (car.x, car.y)
                    if new_position in positions:
                        collided_car = positions[new_position]
                        collision_details.append(
                            f"{car.name}, collides with {collided_car.name} at {new_position} at step {step}"
                        )
                        car.commands = []  # Stop further commands for collided cars
                        car.active = False
                        collided_car.active = False
                        print(f"Collision detected: {car.name} and {collided_car.name} at {new_position}")
                    else:
                        positions[new_position] = car

            print(f"Positions after step {step}: {positions}")
            print(f"Collisions so far: {collision_details}")

        return collision_details

    def get_simulation_result(self, collision_details):
        """Generate the simulation result."""
        if collision_details:
            return "After simulation, the result is:\n" + "\n".join(collision_details)
        else:
            results = "After simulation, no collisions occurred.\nFinal positions:\n"
            results += "\n".join(
                f"- {car.name}, ({car.x},{car.y}) {car.direction}" for car in self.cars
            )
            return results

    def reset_simulation(self):
        """Reset the simulation to start over."""
        self.field = None
        self.cars = []