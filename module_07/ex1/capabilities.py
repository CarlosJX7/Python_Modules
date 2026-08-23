from abc import ABC
from abc import abstractmethod

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass

class TransformCapability(ABC):
    @abstractmethod
    def transform() -> str:
        pass

    @abstractmethod
    def revert() -> str:
        pass
        