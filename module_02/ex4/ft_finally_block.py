class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error Exception") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error Exception") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> bool:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid ñplant name to water: {plant_name}")
    return True


def test_watering_system(plants) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            if water_plant(plant):
                print(f"Watering {plant}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    plants = ("Tomato", "Lettuce", "Carrots")
    print("Testing valid plants...")
    test_watering_system(plants)
    plants = ("Tomato", "lettuce", "Carrots")
    print("Testing invalid plants...")
    test_watering_system(plants)
    print("Cleanup always happens, even with errors!")
