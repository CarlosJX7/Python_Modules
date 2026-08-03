#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self, owner: "Plant") -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.owner = owner

        def show_stats(self) -> None:
            g = self.grow_calls
            a = self.age_calls
            s = self.show_calls
            print(f"[statistics for {self.owner.name.capitalize()}]")
            print(f"Stats: {g} grow, {a} age, {s} show")

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
        self._stats = Plant.Stats(self)

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
        self._stats.show_calls += 1
        name = self.name.capitalize()
        print(f"{name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.set_height(round(self._height + self.ratio, 1))
        self.total += self.ratio
        self._stats.grow_calls += 1

    def age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name.capitalize()}: ", end="")
            print("Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age_days += days
            self._stats.age_calls += 1
            return True

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant")

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
    class TreeStats(Plant.Stats):
        def __init__(self, owner: "Tree") -> None:
            super().__init__(owner)
            self.shade_calls = 0

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
            f"{self.get_height()}cm long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

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


class Seed(Flower):
    pass

def year() -> None:
    print("=== Check year-old")
    days = 30
    print(f"Is {days} more than a year? -> {Plant.check_age(days)}")
    days = 400
    print(f"Is {days} more than a year? -> {Plant.check_age(days)}")

def flower() -> None:
    print("\n=== Flower")
    flower = Flower("rose", 15, 10, 8, 0, "red")
    flower.show()
    flower.show_bloom()
    flower._stats.show_stats()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    flower._stats.show_stats()

def tree() -> None:
    print("\n=== Tree")
    tree = Tree("oak", 200, 365, 0, 0, 5)
    tree.show()
    tree._stats.show_stats()
    #print("[asking the oak to produce shade]")
    #tree.produce_shade()
    #falta gestioar shade_calls en la calse tree

if __name__ == "__main__":
    print("=== Garden statistics ===")
    year()
    flower()
    tree()