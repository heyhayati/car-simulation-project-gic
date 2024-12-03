import pytest
from simulation.field import Field
from exceptions.field_exceptions import InvalidFieldDimensionsError, OutOfBoundsError


def test_field_initialization():
    field = Field(width=10, height=10)
    assert field.width == 10
    assert field.height == 10


def test_invalid_field_dimensions():
    with pytest.raises(InvalidFieldDimensionsError):
        Field(width=-1, height=5)

    with pytest.raises(InvalidFieldDimensionsError):
        Field(width=0, height=0)


def test_field_is_within_bounds():
    field = Field(width=10, height=10)

    # Valid position
    assert field.is_within_bounds(5, 5) is True

    # Out-of-bounds position raises exception
    with pytest.raises(OutOfBoundsError):
        field.is_within_bounds(10, 10)  # Edge case