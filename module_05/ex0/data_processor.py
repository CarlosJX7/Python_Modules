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
        if not self._data_list:
            raise ValueError("No data to output")
        output_data = self._data_list.pop(0)
        output_index = self._index
        self._index += 1
        return (output_index, output_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, (int, float)):
                    return False

        elif not isinstance(data, (int, float)):
            return False

        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Error en ingest de numeric_processor")
        if not isinstance(data, list):
            data_list = [data]
        else:
            data_list = data
        for element in data_list:
            self._data_list.append(str(element))


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

        if not isinstance(data, list):
            data_list = [data]
        else:
            data_list = data
        for string in data_list:
            self._data_list.append(string)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def validate_dict(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            for key, value in d.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for element in data:
                if not validate_dict(element):
                    return False
            return True

        if not isinstance(data, dict):
            return False

        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Error en ingest de Log")

        if not isinstance(data, list):
            list_data = [data]
        else:
            list_data = data

        for element in list_data:
            level = element.get("log_level", "default_level")
            message = element.get("log_message", "default_message")
            self._data_list.append(f"{level}:{message}")
