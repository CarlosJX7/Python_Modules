from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    list_name = [
        "bob",
        "alice",
        "dylan",
        "charlie"
    ]
    list_action = [
        "run",
        "eat",
        "sleep",
        "grab",
        "climb",
        "swim",
        "release",
        "use"
    ]
    while True:
        name = random.choice(list_name)
        action = random.choice(list_action)
        yield name, action


def consume_event(events: list[tuple[str, str]]) -> Generator[
                                    tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    generator = gen_event()
    for i in range(100):
        random_event = next(generator)
        print(
            f"Event {i}: Player {random_event[0]} "
            f"did action {random_event[1]}"
            )

    events: list[tuple[str, str]] = []
    for i in range(10):
        events.append(next(generator))
    print(events)

    for name, event in consume_event(events):
        print(f"Got event from list: ('{name}', '{event}')")
        print(f"Remains in list: {events}")
