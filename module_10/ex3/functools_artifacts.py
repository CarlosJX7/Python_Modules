from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    match operation:
        case "add":
            return reduce(operator.add, spells)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return max(spells)
        case "min":
            return min(spells)
        case _:
            raise ValueError(f"Operation {operation} not found")


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[..., str]]:
    enchantments: dict[str, Callable[..., str]] = {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "water": partial(base_enchantment, 50, "water")
    }
    return enchantments


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"[int] Damage spell {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"[str] Enchantment {spell}"

    @dispatcher.register(list)
    def _(spell: list[Any]) -> str:
        return f"[list] Multicast: {len(spell)} spells"

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Element: {element} with {power} and targeting ---> {target} <---"


if __name__ == "__main__":
    print("===== Spell reducer =====")
    powers = [10, 20, 40, 30]
    print(f"Sum     : {spell_reducer(powers, 'add')}")
    print(f"Product : {spell_reducer(powers, 'multiply')}")
    print(f"Max     : {spell_reducer(powers, 'max')}")

    print("\n===== Partial enchanter =====")
    part_ench = partial_enchanter(base_enchantment)
    print(part_ench["fire"]("Dragon"))
    print(part_ench["ice"]("Goblin"))
    print(part_ench["water"]("Troll"))

    print("\n===== Memoized fibonacci =====")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\n===== Spell dispatcher =====")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "thunder"]))
    print(dispatch(3.14))
