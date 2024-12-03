import pytest
from simulation.simulation import Simulation
from exceptions.field_exceptions import OutOfBoundsError


def test_simulation_initialization():
    sim = Simulation()
    assert sim.field is None
    assert sim.cars == []


def test_create_field():
    sim = Simulation()
    sim.create_field(10, 10)
    assert sim.field.width == 10
    assert sim.field.height == 10


def test_add_car():
    sim = Simulation()
    sim.create_field(10, 10)
    sim.add_car("A", 1, 2, "N", "FFR")
    assert len(sim.cars) == 1
    car = sim.cars[0]
    assert car.name == "A"
    assert car.x == 1
    assert car.y == 2
    assert car.direction == "N"
    assert car.commands == list("FFR")


def test_unique_car_names():
    """Test that car names must be unique in the simulation."""
    sim = Simulation()
    sim.create_field(10, 10)

    # Add the first car with a unique name
    sim.add_car("A", 1, 1, "N", "FF")

    # Attempt to add another car with the same name
    with pytest.raises(ValueError, match="Car name A already exists."):
        sim.add_car("A", 2, 2, "E", "RR")

    # Add another car with a different name
    sim.add_car("B", 3, 3, "S", "LL")

    # Assert that only two cars exist in the simulation
    assert len(sim.cars) == 2
    assert sim.cars[0].name == "A"
    assert sim.cars[1].name == "B"


def test_add_car_out_of_bounds():
    """Test adding a car outside the field bounds."""
    sim = Simulation()
    sim.create_field(10, 10)

    # Add a car outside the field bounds
    with pytest.raises(OutOfBoundsError):
        sim.add_car("A", 11, 2, "N", "FFR")


def test_get_initial_cars():
    sim = Simulation()
    sim.create_field(10, 10)
    sim.add_car("A", 1, 2, "N", "FFR")
    sim.add_car("B", 7, 8, "W", "LLF")
    initial_state = sim.get_initial_cars()
    # Update assertions to match the actual output format
    assert "A, (1,2) N" in initial_state
    assert "B, (7,8) W" in initial_state


def test_simulation_with_single_collision():
    """Test scenario with a single collision between two cars."""
    sim = Simulation()
    sim.create_field(10, 10)
    sim.add_car("A", 1, 2, "N", "FFRFFFFRRL")
    sim.add_car("B", 7, 8, "W", "FFLFFFFFFF")

    # Run simulation
    collision_details = sim.process_commands()

    # Assert the collision details
    assert len(collision_details) == 2
    assert collision_details[0] == "A, collides with B at (5, 4) at step 7"
    assert collision_details[1] == "B, collides with A at (5, 4) at step 7"


def test_simulation_multi_car_collision():
    """Test scenario where A and B collide first, and C collides with A and B later."""
    sim = Simulation()
    sim.create_field(10, 10)

    # Add cars with their initial positions, directions, and commands
    sim.add_car("A", 2, 2, "E", "FFFFLF")
    sim.add_car("B", 6, 6, "S", "FFFFRF")
    sim.add_car("C", 1, 1, "E", "FFFFFF")

    # Run the simulation
    collision_details = sim.process_commands()

    # Expected collision details after the first collision (Step 4)
    expected_collisions = [
        "A, collides with B at (6, 2) at step 4",
        "B, collides with A at (6, 2) at step 4"
    ]

    # Assert collision details match
    assert collision_details == expected_collisions


def test_simulation_two_car_without_collision():
    """Test scenario where two cars move without colliding."""
    sim = Simulation()
    sim.create_field(10, 10)

    # Add cars with their initial positions, directions, and commands
    sim.add_car("A", 1, 1, "E", "FFFF")
    sim.add_car("B", 2, 2, "N", "FFFF")

    # Run the simulation
    collision_details = sim.process_commands()

    # Assert no collisions
    assert len(collision_details) == 0

    # Get final state
    final_state = sim.get_simulation_result(collision_details)

    # Assert final positions and directions
    assert "A, (5,1) E" in final_state
    assert "B, (2,6) N" in final_state


def test_simulation_multiple_no_collision():
    """Test scenario where 4 cars move around without colliding."""
    sim = Simulation()
    sim.create_field(10, 10)

    # Add cars with their initial positions, directions, and commands
    sim.add_car("A", 1, 1, "E", "FFFF")
    sim.add_car("B", 9, 9, "W", "FFFF")
    sim.add_car("C", 1, 9, "S", "FFFF")
    sim.add_car("D", 9, 1, "N", "FFFF")

    # Run the simulation
    collision_details = sim.process_commands()

    # Ensure no collisions occurred
    assert collision_details == []

    # Verify final positions of the cars
    final_state = sim.get_simulation_result(collision_details)
    expected_final_positions = [
        "- A, (5,1) E",
        "- B, (5,9) W",
        "- C, (1,5) S",
        "- D, (9,5) N",
    ]
    for expected_position in expected_final_positions:
        assert expected_position in final_state

    # Ensure the output indicates no collisions
    assert "no collisions occurred" in final_state.lower()


def test_full_rotation_cycle():
    """Test full rotation cycle (4 turns return to original direction)."""
    sim = Simulation()
    sim.create_field(5, 5)

    # Add a car facing North and rotate left 4 times
    sim.add_car("A", 2, 2, "N", "LLLL")  # Full 360-degree turn (N -> W -> S -> E -> N)
    collision_details = sim.process_commands()
    assert collision_details == []  # No collision expected
    final_state = sim.get_simulation_result(collision_details)
    assert "A, (2,2) N" in final_state  # Final direction should be North

    # Add a car facing North and rotate right 4 times
    sim.add_car("B", 3, 3, "N", "RRRR")  # Full 360-degree turn (N -> E -> S -> W -> N)
    collision_details = sim.process_commands()
    assert collision_details == []  # No collision expected
    final_state = sim.get_simulation_result(collision_details)
    assert "B, (3,3) N" in final_state  # Final direction should be North


def test_rotation_with_collision():
    """Test rotation commands followed by a collision."""
    sim = Simulation()
    sim.create_field(5, 5)

    # Add two cars that will collide after rotation
    sim.add_car("A", 2, 2, "N", "LF")  # Turn left (West), move forward to (1,2)
    sim.add_car("B", 1, 3, "E", "RF")  # Turn right (South), move forward to (1,2)
    collision_details = sim.process_commands()

    # Expected collision details
    expected_collisions = [
        "A, collides with B at (1, 2) at step 2",
        "B, collides with A at (1, 2) at step 2",
    ]

    assert collision_details == expected_collisions  # Validate collisions
    final_state = sim.get_simulation_result(collision_details)
    assert "A, (1,2) W" in final_state
    assert "B, (1,2) S" in final_state


def test_simulation_reset():
    sim = Simulation()
    sim.create_field(10, 10)
    sim.add_car("A", 1, 2, "N", "FFR")
    sim.reset_simulation()
    assert sim.field is None
    assert sim.cars == []
