#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float = 0.0,
            age_days: int = 0,
            ratio: float = 0.0,
            total: float = 0.0
            ) -> None:
        self.name = name
        self.ratio = float(ratio)
        self.total = float(total)
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float) -> bool:
        heigth = float(height)
        if heigth < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, height can't be negative")
            print("Height update rejected")
            return False
        else:
            self._height = float(heigth)
            return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age_days = age
            return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.set_height(round(self._height + self.ratio, 1))
        self.total += self.ratio

    def age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age_days += days
            return True


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("rose", 15, 10)
    print("Plant created: ", end="")
    plant1.show()
    if plant1.set_height(25):
        print(f"\nHeight updated: {plant1.get_height()}cm")
    if plant1.set_age(30):
        print(f"Age updated: {plant1.get_age()} days\n")
    plant1.set_age(-1)
    plant1.set_height(-1)
    print("\nCurrent state: ", end="")
    plant1.show()
