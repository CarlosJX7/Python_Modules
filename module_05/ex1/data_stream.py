from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data_list: list[str] = []
        self._index: int = 0
        self._process_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
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
            raise ValueError("Improper numeric data")
        if not isinstance(data, list):
            data_list = [data]
        else:
            data_list = data
        for element in data_list:
            self._data_list.append(str(element))
            self._process_count += 1

    @property
    def name(self) -> str:
        return "Numeric Processor"


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
            raise ValueError("Improper text data")

        if not isinstance(data, list):
            data_list = [data]
        else:
            data_list = data
        for string in data_list:
            self._data_list.append(string)
            self._process_count += 1

    @property
    def name(self) -> str:
        return "Text Processor"


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

        return validate_dict(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if not isinstance(data, list):
            list_data = [data]
        else:
            list_data = data

        for element in list_data:
            level = element.get("log_level", "")
            message = element.get("log_message", "")
            self._data_list.append(f"{level}: {message}")
            self._process_count += 1

    @property
    def name(self) -> str:
        return "Log Processor"


class DataStream:
    def __init__(self) -> None:
        self._processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise ValueError("invalid data stream input")
        self._processor_list.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        def find_process(element: list[typing.Any]) -> bool:
            for proc in self._processor_list:
                if proc.validate(element):
                    proc.ingest(element)
                    return True
            raise ValueError(f"Can't process element in stream: '{element}'")

        for data in stream:
            try:
                find_process(data)
            except ValueError as e:
                print(f"DataStream error - {e}")

    def print_processors_stats(self) -> None:
        if not self._processor_list:
            print("No processor found, no data")
            return
        for proc in self._processor_list:
            print(
                f"{proc.name}: total {proc._process_count} items processed, "
                f"remaining {len(proc._data_list)} on processor"
                )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("Initialize Data Stream...")
    proc_list: DataStream = DataStream()

    print("== DataStream statistics ==")
    proc_list.print_processors_stats()

    print("\nRegistering Numeric Processor")
    number_proc = NumericProcessor()
    proc_list.register_processor(number_proc)

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {data}")
    proc_list.process_stream(data)
    proc_list.print_processors_stats()

    print("\n== DataStream statistics ==")
    proc_list.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    proc_list.register_processor(text_proc)
    proc_list.register_processor(log_proc)

    print("Send the same batch again")
    proc_list.process_stream(data)

    print("\n== DataStream statistics ==")
    proc_list.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
        )
    consume_dict = {
        "Numeric Processor": 3,
        "Text Processor": 2,
        "Log Processor": 1,
        }
    for proc in proc_list._processor_list:
        elements = consume_dict.get(proc.name, 0)
        for _ in range(elements):
            try:
                proc.output()
            except ValueError as msg:
                print(msg)
                break

    print("\n== DataStream statistics ==")
    proc_list.print_processors_stats()
