from simulation.car import Car
from simulation.field import Field

from exceptions.field_exceptions import InvalidFieldDimensionsError
from exceptions.car_exceptions import InvalidCarCommandError, CarCollisionError


class Simulation:
    def __init__(self):
        self.field = None
        self.cars = []

    def create_field(self, width, height):
        """Create the field with the given width and height."""
        if width <= 0 or height <= 0:
            raise InvalidFieldDimensionsError("Field dimensions must be greater than zero.")
        self.field = Field(width, height)

    def add_car(self, name, x, y, direction, commands):
        """Add a car to the field."""
        if not self.field.is_within_bounds(x, y):
            raise ValueError(f"Car {name} position ({x}, {y}) is out of bounds.")
        if any(car.name == name for car in self.cars):
            raise ValueError(f"Car name {name} already exists.")
        if not all(command in {"L", "R", "F"} for command in commands):
            raise InvalidCarCommandError(f"Invalid commands for car {name}: {commands}")
        new_car = Car(name, x, y, direction)
        new_car.commands = list(commands)
        self.cars.append(new_car)

    def reset_simulation(self):
        """Reset the simulation to start over."""
        self.field = None
        self.cars = []

    def get_initial_cars(self):
        """Return the initial list of cars in the field."""
        if not self.cars:
            return "No cars have been added to the field yet."
        return "\n".join(str(car) for car in self.cars)

    def process_commands(self):
        """Run simulation step by step, detecting collisions and logging all collisions."""
        if not self.cars:
            return []

        collision_details = []  # Store collision logs
        step = 0

        while any(car.commands for car in self.cars):  # Continue as long as at least one car has commands
            step += 1
            positions = {}  # Tracks positions for this step

            for car in self.cars:
                if car.commands and car.active:  # Only process active cars that still have commands
                    command = car.commands.pop(0)
                    car.execute_command(command, self.field.width, self.field.height)

                # Check for collisions with other cars
                new_position = (car.x, car.y)

                if new_position in positions:
                    # Log collisions for all cars at this position
                    for collided_car in positions[new_position]:
                        if collided_car.active:  # Only process active cars
                            collision_details.append(
                                f"{car.name}, collides with {collided_car.name} at {new_position} at step {step}"
                            )
                            collision_details.append(
                                f"{collided_car.name}, collides with {car.name} at {new_position} at step {step}"
                            )

                            # Mark all involved cars as inactive and clear their commands
                            collided_car.commands = []
                            collided_car.active = False

                    # Mark the current car as inactive and clear its commands
                    car.commands = []
                    car.active = False

                # If no collision, track the car's position
                if new_position not in positions:
                    positions[new_position] = []
                positions[new_position].append(car)

        # Sort collision details alphabetically before returning
        collision_details = sorted(collision_details, key=lambda col: col.split(",")[0])
        return collision_details

    def get_simulation_result(self, collision_details):
        """Generate the final simulation result."""
        result = []

        if collision_details:
            result.append("Collision detected:")
            result.extend(collision_details)
        else:
            result.append("After simulation, no collisions occurred.")
            result.append("Final positions:")

        for car in self.cars:
            result.append(f"- {car}")

        return "\n".join(result)
