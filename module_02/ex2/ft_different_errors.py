def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        value = int("abc")
    if operation_number == 1:
        value = 1 / 0
    if operation_number == 2:
        value = open("/non/existing/file")
    if operation_number == 3:
        value = "a" + 1
    if operation_number == 4:
        value = 1 + 1


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for test in range(5):
        print(f"Testing operation {test}...")
        try:
            garden_operations(test)
            print("Operation completed succesfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
