from .simulation_exceptions import SimulationError

class InvalidFieldDimensionsError(SimulationError):
    """Raised when the field dimensions are invalid."""
    def __init__(self, width, height, message="Invalid field dimensions."):
        self.width = width
        self.height = height
        super().__init__(f"{message} Dimensions: {width}x{height}")

class OutOfBoundsError(SimulationError):
    """Raised when a car tries to move outside the field boundaries."""
    def __init__(self, position, message="Car is out of field bounds."):
        self.position = position
        super().__init__(f"{message} Position: {position}")
