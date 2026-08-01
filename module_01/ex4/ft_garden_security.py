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

        self.set_heigth(height)
        self.set_age(age_days)

    def set_heigth(self, heigth: float) -> None:
        heigth = float(heigth)
        if heigth < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, height can't be negative")
            print("Heigth update rejected")
            return
        else:
            self._height = float(heigth)

    def set_age(self, age: int) -> None:
        age_days = float(age)
        if age_days < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._age_days = age_days

    def get_heigth (self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._age_days

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.get_heigth()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.ratio, 1)
        self.total += self.ratio

    def age(self, days: int) -> None:
        self.age_days += days


if __name__ == "__main__":
    plant1 = Plant("rose", -25, -30)
    plant1.show()