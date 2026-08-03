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


class Flower(Plant):
    def __init__(
            self, name: str,
            height: float = 0,
            age_days: int = 0,
            ratio: float = 0,
            total: float = 0,
            color: str = "Unknown",
            blooming: bool = False
            ) -> None:
        super().__init__(name, height, age_days, ratio, total)
        self.color = color
        self.blooming = blooming

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def show_bloom(self) -> None:
        if self.blooming is True:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self, name: str,
            height: float = 0,
            age_days: int = 0,
            ratio: float = 0,
            total: float = 0,
            trunk_diameter: float = 0.0,
            shade: int = 0
            ) -> None:
        super().__init__(name, height, age_days, ratio, total)
        self.trunk_diameter = float(trunk_diameter)
        self.shade = shade

    def produce_shade(self) -> None:
        self.shade += 1
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.get_height()}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
            self, name: str,
            height: float = 0,
            age_days: int = 0,
            ratio: float = 0,
            total: float = 0,
            harvest_season: str = "Unknown",
            nutritional_value: int = 0
            ) -> None:
        super().__init__(name, height, age_days, ratio, total)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def nutritional_val(self) -> None:
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("rose", 15.0, 10, 0, 0, "red")
    flower.show()
    flower.show_bloom()
    print(f"[asking the {flower.name} to bloom]")
    flower.bloom()
    flower.show_bloom()
    print("=== Tree")
    tree = Tree("oak", 200.0, 365, 0, 0, 5)
    print(f"Trunk diameter: {tree.trunk_diameter}")
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    print("=== Vegetable")
    vegetable = Vegetable("tomato", 5, 10, 2.1, 0, "April", 0)
    vegetable.show()
    days = 20
    print(f"[make {vegetable.name} grow and age for {days} days]")
    for i in range(days):
        vegetable.grow()
        vegetable.age(1)
        vegetable.nutritional_val()
    vegetable.show()
