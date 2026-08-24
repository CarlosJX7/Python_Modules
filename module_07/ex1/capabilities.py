from abc import ABC
from abc import abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
