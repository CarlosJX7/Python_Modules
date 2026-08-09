import math


def print_coordinates(data: tuple[float, float, float]) -> None:
    x = data[0]
    y = data[1]
    z = data[2]
    print(f"It includes: X = {x}, Y = {y}, Z = {z}")


def distance_center(
                    first: tuple[float, float, float],
                    second: tuple[float, float, float] = (0, 0, 0)
                    ) -> float:
    total = 0.0
    for i in (0, 1, 2):
        total = (first[i] - second[i])**2 + total
    distance = math.sqrt(total)
    return round(distance, 4)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data_str = input("Enter new coordinates as floats in format 'x,y,z': ")
        raw_coordinates = data_str.split(",")
        try:
            if len(raw_coordinates) != 3:
                raise ValueError("Invalid syntax")
            data = (
                    float(raw_coordinates[0]),
                    float(raw_coordinates[1]),
                    float(raw_coordinates[2])
                    )
            return data
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print_coordinates(first)
    print(f"Distance to center: {distance_center(first)}")
    print("\nGet a second set of coordinates")
    second = get_player_pos()
    print_coordinates(second)
    print(
        f"Distance between the 2 sets of coordinates "
        f"{distance_center(first, second)}"
        )

