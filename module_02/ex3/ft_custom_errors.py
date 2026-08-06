class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error Exception") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error Exception") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error Exception") -> None:
        super().__init__(message)


def plant_error(wilting: bool) -> None:
    if wilting:
        raise PlantError("The tomato plant is wilting!")


def water_error(volume: float) -> None:
    if volume <  1:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        plant_error(False)
        plant_error(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError....")
    try:
        water_error(1)
        water_error(0.5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        plant_error(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_error(0.5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
