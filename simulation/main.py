from simulation import Simulation
import sys
import os

def main():

    sim = Simulation()

    while True:
        print("\nWelcome to Auto Driving Car Simulation!")
        print("[1] Create field\n[2] Add car\n[3] Run simulation\n[4] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            width, height = map(int, input("Enter field dimensions (width height): ").split())
            sim.create_field(width, height)
        elif choice == '2':
            name = input("Enter car name: ")
            x, y, direction = input("Enter initial position (x y direction): ").split()
            commands = input("Enter command sequence (L, R, F): ")
            sim.add_car(name, int(x), int(y), direction, commands)
        elif choice == '3':
            sim.process_commands()
            sim.show_results()
        elif choice == '4':
            print("Exiting simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print(f"Current Working Directory: {os.getcwd()}")
    main()
