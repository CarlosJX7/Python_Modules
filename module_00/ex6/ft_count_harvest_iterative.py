def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    day = int(1)
    while day <= harvest:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
