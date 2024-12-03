from exceptions.field_exceptions import InvalidFieldDimensionsError, OutOfBoundsError

class Field:
    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise InvalidFieldDimensionsError(width, height)
        self.width = width
        self.height = height

    def is_within_bounds(self, x: int, y: int) -> bool:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise OutOfBoundsError((x, y))
        return True