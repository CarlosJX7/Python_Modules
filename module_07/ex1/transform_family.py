from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self.transformed: bool = False
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self.transformed: bool = False
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
