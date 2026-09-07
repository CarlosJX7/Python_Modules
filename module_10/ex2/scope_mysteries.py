from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    total_calls = 0

    def func_counter() -> int:
        nonlocal total_calls
        total_calls += 1
        return total_calls
    return func_counter


if __name__ == "__main__":
    func1 = mage_counter()
    func2 = mage_counter()

    print(f"Function 1 called: {func1()}")
    print(f"Function 2 called: {func2()}")
    print(f"Function 2 called: {func2()}")
    print(f"Function 1 called: {func1()}")
