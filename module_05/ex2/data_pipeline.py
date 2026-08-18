from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        line = ",".join(value for _, value in data)
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts: list[str] = []
        for index, value in data:
            parts.append(f'"item_{index}": "{value}"')
        json_str = "{" + ", ".join(parts) + "}"
        print("JSON Output:")
        print(json_str)


class DataStream:
    def __init__(self) -> None:
        self._processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise ValueError("invalid data stream input")
        self._processor_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        def find_process(element: list[Any]) -> bool:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume up to nb items per processor
        and send each batch to plugin."""
        if not nb:
            return

        for proc in self._processor_list:
            output_list: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    output_list.append(proc.output())
                except ValueError:
                    break
            plugin.process_output(output_list)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    data_stream = DataStream()

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("Registering Processors")
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(numeric_proc)
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING", "log_message":
                "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch1}")
    data_stream.process_stream(batch1)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_procesor = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_procesor)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {batch2}")
    data_stream.process_stream(batch2)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
