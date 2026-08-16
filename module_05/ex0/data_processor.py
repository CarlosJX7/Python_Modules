from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data_list: list[str] = []
        self._index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        output_data = self._data_list.pop()
        output_index = self._index
        self._index += 1
        return (output_index, output_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, (int, float)):
                    return False

        elif not isinstance(data, (int, float)) :
            return False

        return True


    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Error en ingest de numeric_processor")

        if isinstance(data, list):
            for element in data:
                self._data_list.append(str(element))

        else:
            self._data_list.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for string in data:
                if not isinstance(string, str):
                    return False

        elif not isinstance(data, str):
            return False

        return True


    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Error en inges de text processor")

        if isinstance(data, list):
            for string in data:
                self._data_list.append(string)
        else:
            self._data_list.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False

        if not isinstance(data, dict):
            return False

        return True


    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise ValueError("Error en ingest de Log")

        if isinstance(data, list):
            for element in data:
                for string in element.values():
                    self._data_list.append(string)

        if isinstance(data, dict):
            for string in data.values():
                self._data_list.append(string)

