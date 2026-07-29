#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name = "Rose"
    height = int(25)
    age = int(30)
    print(f"""\
=== Welcome to My Garden ===
Plant: {name}
Height: {height}
Age: {age}
=== End of Program ===""")


if __name__ == "__main__":
    ft_garden_intro()
