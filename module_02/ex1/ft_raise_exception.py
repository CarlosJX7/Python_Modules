def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp} is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker===")
    data = ("25", "abc", "100", "-50")
    for d in data:
        try:
            print(f"Input data is '{d}'")
            temperature = input_temperature(d)
            print(f"The input data is now '{temperature}C'\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
