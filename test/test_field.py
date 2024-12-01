import pytest
from field import Field

@pytest.fixture
def field():
    return Field(width=10, height=10)

def test_is_within_bounds(field):
    assert field.is_within_bounds(5, 5) is True
    assert field.is_within_bounds(10, 10) is False
    assert field.is_within_bounds(-1, 5) is False
    assert field.is_within_bounds(5, -1) is False
