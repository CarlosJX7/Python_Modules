#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            ratio: float = 0.0,
            total: float = 0.0
            ) -> None:
        self.name = name
        self.height = float(height)
        self.age_days = age_days
        self.ratio = float(ratio)
        self.total = float(total)

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.ratio, 1)
        self.total += self.ratio

    def age(self, days: int) -> None:
        self.age_days += days


if __name__ == "__main__":
    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
