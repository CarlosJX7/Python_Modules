from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                                        f"Invalid Creature "
                                        f"'{creature.name}' for this strategy"
                                        )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                                        f"Invalid Creature '{creature.name}' "
                                        f"for this aggressive strategy"
                                        )
        print(cast(TransformCapability, creature).transform())
        print(creature.attack())
        print(cast(TransformCapability, creature).revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                                        f"Invalid Creature '{creature.name}' "
                                        f"for this defensive strategy"
                                        )
        print(creature.attack())
        print(cast(HealCapability, creature).heal())


class InvalidStrategyError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
