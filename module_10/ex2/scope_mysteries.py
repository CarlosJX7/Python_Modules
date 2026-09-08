from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    total_calls = 0

    def func_counter() -> int:
        nonlocal total_calls
        total_calls += 1
        return total_calls
    return func_counter

def spell_accumulator(initial_power: int)-> Callable[[int], int]:
    power = initial_power
    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


if __name__ == "__main__":
    func1 = mage_counter()
    func2 = mage_counter()

    print(f"Function 1 called: {func1()}")
    print(f"Function 2 called: {func2()}")
    print(f"Function 2 called: {func2()}")
    print(f"Function 1 called: {func1()}")

    func1 = spell_accumulator(20)
    func2 = spell_accumulator(20)

    print(f"Function 1 called: {func1(1)}")
    print(f"Function 2 called: {func2(1)}")
    print(f"Function 2 called: {func2(10)}")
    print(f"Function 1 called: {func1(10)}")
