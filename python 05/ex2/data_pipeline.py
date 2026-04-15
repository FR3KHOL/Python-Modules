import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.total_processed: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise Exception("No data to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(x, (int, float))
                                          for x in data):
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append((self.total_processed, str(item)))
                self.total_processed += 1
        else:
            self.storage.append((self.total_processed, str(data)))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.storage.append((self.total_processed, str(item)))
                self.total_processed += 1
        else:
            self.storage.append((self.total_processed, str(data)))
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        if isinstance(data, list):
            return all(isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()) for d in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for item in data:
                lvl = item.get('log_level', '')
                msg = item.get('log_message', '')
                self.storage.append((self.total_processed, f"{lvl}: {msg}"))
                self.total_processed += 1
        else:
            lvl = data.get('log_level', '')
            msg = data.get('log_message', '')
            self.storage.append((self.total_processed, f"{lvl}: {msg}"))
            self.total_processed += 1


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        strings = [item[1] for item in data]
        print(",".join(strings))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("{" + ", ".join(items) + "}")


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error Can't process element: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for p in self.processors:
            n = p.__class__.__name__.replace("Processor", " Processor")
            print(f"{n}: total {p.total_processed} items processed, "
                  f"remaining {len(p.storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted = []
            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except Exception:
                    break
            if extracted:
                plugin.process_output(extracted)


if __name__ == "__main__":
    print("=== Code Nexus Data Pipeline ===")
    print("\nInitialize Data Stream")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("\nSend first batch of data on stream:", end="")
    batch1 = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access!'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']
    ]
    print(f"{batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExport()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    print("\nSend another batch of data:", end="")
    batch2 = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello'
    ]
    print(f"{batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExport()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
