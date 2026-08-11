import sys


def contains_list(item: str, inventory: dict[str, int]) -> bool:
    for name in inventory:
        if item == name:
            return True
    return False


def total_quantity(inventory: dict[str, int]) -> int:
    total = 0
    for item in inventory:
        total += int(inventory[item])
    return total


def get_max(inventory: dict[str, int]) -> tuple[str, int]:
    names = list(inventory.keys())
    max_item = names[0]
    max_value = inventory[max_item]

    for item in inventory:
        if max_value < inventory[item]:
            max_item = item
            max_value = inventory[item]
    return max_item, max_value


def get_min(inventory: dict[str, int]) -> tuple[str, int]:
    names = list(inventory.keys())
    min_item = names[0]
    min_value = inventory[min_item]

    for item in inventory:
        if min_value > inventory[item]:
            min_item = item
            min_value = inventory[item]
    return min_item, min_value


def get_percentage(quantity: int, total: int) -> float:
    return round(quantity / total * 100, 1)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter: '{parts[0]}'")
            continue
        if contains_list(parts[0], inventory):
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[str(parts[0])] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[1]}: {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(
        f"Total quantity of the {len(inventory)} "
        f"items: {total_quantity(inventory)}")
    for item in inventory:
        print(
            f"Item {item} represents "
            f"{get_percentage((inventory[item]), total_quantity(inventory))}%")
    max_item = get_max(inventory)
    min_item = get_min(inventory)
    print(f"Item most abundant: {max_item[0]} with quantity {max_item[1]}")
    print(f"Item least abundant: {min_item[0]} with quantity {min_item[1]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
