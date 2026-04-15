import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.queue: list[tuple[int, str]] = []
        self.total_processed: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.queue:
            raise Exception("No data left to output")
        return self.queue.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float))
                       and not isinstance(x, bool) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.queue.append((self.total_processed, str(item)))
                self.total_processed += 1
        else:
            self.queue.append((self.total_processed, str(data)))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.queue.append((self.total_processed, item))
                self.total_processed += 1
        else:
            self.queue.append((self.total_processed, data))
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def is_valid_dict(d: typing.Any) -> bool:
            return (isinstance(d, dict) and all(isinstance(k, str)
                    and isinstance(v, str) for k, v in d.items()))

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(isinstance(x, dict) and is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            if "log_level" in d and "log_message" in d:
                return f"{d['log_level']}: {d['log_message']}"
            return str(d)

        if isinstance(data, list):
            for item in data:
                self.queue.append((self.total_processed, format_log(item)))
                self.total_processed += 1
        else:
            self.queue.append((self.total_processed, format_log(data)))
            self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print("DataStream error Can't process"
                      f" element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.total_processed} items processed,"
                  f" remaining {len(proc.queue)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus Data Stream ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch = [
        "Hello world",
        [3.14, 1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nConsume some elements "
          "from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        txt_proc.output()
    for _ in range(1):
        log_proc.output()

    stream.print_processors_stats()
