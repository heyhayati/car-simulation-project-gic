from simulation.simulation import Simulation
from exceptions.field_exceptions import InvalidFieldDimensionsError
from exceptions.car_exceptions import InvalidCarCommandError, CarCollisionError


def main():
    simulation = Simulation()

    while True:
        print("Welcome to Auto Driving Car Simulation!")
        print("Please enter the width and height of the simulation field in x y format:")

        # Initialize the field
        while True:
            try:
                dimensions = input("Enter field dimensions: ").strip().split()
                if len(dimensions) != 2:
                    raise ValueError("Please provide exactly two numbers for the dimensions.")
                width, height = map(int, dimensions)
                simulation.create_field(width, height)
                print(f"You have created a field of {width} x {height}.\n")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
            except InvalidFieldDimensionsError as e:
                print(f"Error: {e}")

        while True:
            try:
                print("\nPlease choose from the following options:")
                print("[1] Add a car to field")
                print("[2] Run simulation")
                choice = input("Enter your choice: ").strip()

                if choice == '1':
                    # Add a car to the field
                    name = input("Please enter the name of the car: ").strip()
                    x, y, direction = input(
                        f"Please enter initial position of car {name} in x y Direction format: "
                    ).split()
                    x, y = int(x), int(y)
                    commands = input(f"Please enter the commands for car {name}: ").strip()
                    simulation.add_car(name, x, y, direction, commands)

                    # Print the current list of cars after adding the new car
                    print("\nYour current list of cars are:")
                    print(simulation.get_initial_cars())

                elif choice == '2':
                    # Print the current list of cars before running the simulation
                    print("\nYour current list of cars are:")
                    print(simulation.get_initial_cars())

                    # Run the simulation
                    print("\nStarting simulation...\n")
                    collision_details = simulation.process_commands()
                    print(simulation.get_simulation_result(collision_details))
                    break

                else:
                    print("Invalid choice. Please select either 1 or 2.\n")

            except InvalidCarCommandError as e:
                print(f"Error: {e}")
            except CarCollisionError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        # Post-simulation options
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            post_choice = input("Enter your choice: ").strip()

            if post_choice == '1':
                # Use reset_simulation to clear the state
                simulation.reset_simulation()
                print("\nSimulation reset. Starting over...\n")
                break
            elif post_choice == '2':
                # Exit the program
                print("Thank you for running the simulation. Goodbye!")
                return
            else:
                print("Invalid choice. Please select either 1 or 2.\n")


if __name__ == "__main__":
    main()
