def _ft_count(current_day: int, harvest_time: int) -> None:
    if current_day > harvest_time:
        print("Harvest time!")
        return
    else:
        print(f"Day {current_day}")
        _ft_count(current_day + 1, harvest_time)


def ft_count_harvest_recursive() -> None:
    harvest_time = int(input("Days until harvest: "))
    _ft_count(1, harvest_time)
