from .creature_factory import CreatureFactory
from .creature import Creature, Aquabub, Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
