def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    data = ("25", "abc")
    for d in data:
        try:
            print(f"Input data is '{d}'")
            temperature = input_temperature(d)
            print(f"The input data is now '{temperature}°C'")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()