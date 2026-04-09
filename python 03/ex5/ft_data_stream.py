import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release", "use"]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while event_list:
        idx = random.randint(0, len(event_list) - 1)
        yield event_list.pop(idx)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events = [next(event_stream) for i in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    consume_ev = consume_event(ten_events)
    for e in consume_ev:
        print(f"Got event from list: {e}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
