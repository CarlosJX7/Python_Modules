import math


def get_player_pos() -> tuple:
    print("Enter new coordinates as floats in format 'x,y,z': hello world")
    coordinates = tuple(input())
    return coordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    x = float(coordinates[0])
    y = float(coordinates[2])
    z = float(coordinates[4])
    print(f"x = {x}, y = {y}, z = {z}")