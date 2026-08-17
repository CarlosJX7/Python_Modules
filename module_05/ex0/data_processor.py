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
            raise ValueError("Improper data input")
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
            raise ValueError("Improper data input")

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
            raise ValueError("Improper data input")

        if not isinstance(data, list):
            list_data = [data]
        else:
            list_data = data

        for element in list_data:
            level = element.get("log_level", "default_level")
            message = element.get("log_message", "default_message")
            self._data_list.append(f"{level}: {message}")


def test_log() -> None:
    print("\nTesting Log Processor...")
    data_list = ["Hello", [{"log_level": "NOTICE", "log_message": "Connection to server"},
                        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]]
    processor = LogProcessor()
    print(f"Trying to validate input '{data_list[0]}: '"
        f"{processor.validate(data_list[0])}")
    print(f"Processing data: {data_list[1]}")
    processor.ingest(data_list[1])
    size = 2
    print(f"Extracting {size} values...")
    for i in range(size):
        try:
            extracted = processor.output()
        except ValueError as e:
            print(f"Got exception: {e}")
            break
        else:
            print(f"Log entry {extracted[0]}: {extracted[1]}")


def test_text() -> None:
    print("\nTesting Text Processor...")
    data_list = [42, ["Hello", "Nexus", "World"]]
    processor = TextProcessor()
    print(f"Trying to validate input '{data_list[0]}':"
        f"{processor.validate(data_list[0])}")
    print(f"Processing data: {data_list[-1]}")
    processor.ingest(data_list[-1])
    size = 1
    print(f"Extracting {size} value...")
    for i in range(size):
        try:
            extracted = processor.output()
        except ValueError as e:
            print(f"Got exception: {e}")
            break
        else:
            print(f"Text value {extracted[0]}: {extracted[1]}")

def test_numeric() -> None:
    print("Testing numeric processor...")
    data_list = [42, "Hello", "foo", [1, 2, 3, 4, 5]]
    processor = NumericProcessor()
    for data in data_list[:2]:
        print(f"Trying to validate '{data}': {processor.validate(data)}")
    print(f"Test invalid ingestion of string '{data_list[2]}' without prior validation:")
    try:
        processor.ingest(data_list[2])
    except ValueError as e:
        print(f"Got exception: {e}")

    print(f"Processing data: {data_list[-1]}")
    processor.validate(data_list[-1])
    processor.ingest(data_list[-1])
    size = 3
    print(f"Extracting {size} values...")
    for i in range(0, size):
        try:
            extracted = processor.output()
        except ValueError as e:
            print(f"Got exception: {e}")
            break
        else:
            print(f"Numeric value: {extracted[0]}: {extracted[1]}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    test_numeric()
    test_text()
    test_log()