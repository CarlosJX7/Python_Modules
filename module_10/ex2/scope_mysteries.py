from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    total_calls = 0

    def func_counter() -> int:
        nonlocal total_calls
        total_calls += 1
        return total_calls
    return func_counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def add_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return add_enchantment


def memory_vault() -> dict[str, Callable[..., object]]:
    vault: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        vault[key] = value

    def recall(key: str) -> object:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("===== Mage counter =====")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\n===== Spell accumulator =====")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\n===== Enchantment factory =====")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\n===== Memory vault =====")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
