#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            ratio: float,
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
    plant1 = Plant("rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant1.grow()
        plant1.age(1)
        plant1.show()
    print(f"Growth this week: {plant1.total}cm")
