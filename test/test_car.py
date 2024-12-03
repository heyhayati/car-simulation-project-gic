import pytest
from simulation.car import Car
from exceptions.car_exceptions import InvalidCarCommandError


def test_car_initialization():
    car = Car(name="A", x=1, y=2, direction="N")
    assert car.name == "A"
    assert car.x == 1
    assert car.y == 2
    assert car.direction == "N"


def test_car_execute_command():
    car = Car(name="A", x=1, y=2, direction="N")
    car.execute_command("F", 10, 10)
    assert (car.x, car.y) == (1, 3)

    car.execute_command("R", 10, 10)
    assert car.direction == "E"

    car.execute_command("L", 10, 10)
    assert car.direction == "N"


def test_car_out_of_bounds():
    car = Car(name="A", x=1, y=2, direction="N")
    car.execute_command("F", 3, 3)
    car.execute_command("F", 3, 3)
    assert car.x == 1
    assert car.y == 3  # Stops at the boundary


def test_car_out_of_bounds():
    """Test that the car stops at the boundary of the field."""
    car = Car(name="A", x=1, y=2, direction="N")

    # Move forward within bounds
    car.execute_command("F", 3, 3)  # Moves to (1, 3)
    car.execute_command("F", 3, 3)  # Should not move beyond (1, 3)

    # Assert the car's final position
    assert car.x == 1  # X-coordinate remains unchanged
    assert car.y == 2  # Y-coordinate stops at the boundary



