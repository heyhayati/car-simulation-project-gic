import pytest
from car import Car

@pytest.fixture
def car():
    return Car(name="A", x=1, y=2, direction="N")

def test_turn_left(car):
    car.turn_left()
    assert car.direction == "W"

def test_turn_right(car):
    car.turn_right()
    assert car.direction == "E"

def test_move_forward_within_bounds(car):
    car.move_forward(10, 10)
    assert (car.x, car.y) == (1, 3)

def test_move_forward_out_of_bounds():
    car = Car(name="B", x=0, y=0, direction="S")
    car.move_forward(10, 10)
    assert (car.x, car.y) == (0, 0)

def test_execute_command_left(car):
    car.execute_command('L', 10, 10)
    assert car.direction == "W"

def test_execute_command_right(car):
    car.execute_command('R', 10, 10)
    assert car.direction == "E"

def test_execute_command_forward(car):
    car.execute_command('F', 10, 10)
    assert (car.x, car.y) == (1, 3)
