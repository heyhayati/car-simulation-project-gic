import pytest
from simulation import Simulation

@pytest.fixture
def simulation():
    sim = Simulation()
    sim.create_field(10, 10)
    return sim

def test_create_field(simulation):
    assert simulation.field.width == 10
    assert simulation.field.height == 10

def test_add_car(simulation):
    simulation.add_car(name="A", x=1, y=2, direction="N", commands="FFR")
    assert len(simulation.cars) == 1
    assert simulation.cars[0].name == "A"
    assert simulation.cars[0].commands == ['F', 'F', 'R']

def test_car_out_of_bounds():
    sim = Simulation()
    sim.create_field(5, 5)
    with pytest.raises(ValueError):
        sim.add_car(name="B", x=6, y=6, direction="E", commands="FFF")

def test_process_commands_no_collision(simulation):
    simulation.add_car(name="A", x=1, y=1, direction="N", commands="FF")
    simulation.process_commands()
    assert (simulation.cars[0].x, simulation.cars[0].y) == (1, 3)
    assert simulation.cars[0].direction == "N"

def test_collision_handling(simulation):
    simulation.add_car(name="A", x=1, y=1, direction="E", commands="FFF")
    simulation.add_car(name="B", x=4, y=1, direction="W", commands="FFF")
    simulation.process_commands()
    assert simulation.cars[0].active is False
    assert simulation.cars[1].active is False
    assert (simulation.cars[0].x, simulation.cars[0].y) == (3, 1)
    assert (simulation.cars[1].x, simulation.cars[1].y) == (3, 1)

def test_show_results(simulation, capsys):
    simulation.add_car(name="A", x=1, y=1, direction="N", commands="F")
    simulation.process_commands()
    simulation.show_results()
    captured = capsys.readouterr()
    assert "A, (1,2) N" in captured.out
