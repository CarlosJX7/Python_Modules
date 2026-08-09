def distinct(data: list[set]) -> set:
        items = set()
        for d in data:
            items = items.union(d)
        return items


def intersection(data: list[set]) -> set:
    return set.intersection(*data)


def unique(player_data: set, data: list[set]) -> set:
    return player_data.difference(*data)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    players = {
        "Alice": {'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer'},
        "Bob": {'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable'},
        "Charlie": {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'FirstSteps', 'Collector Supreme', 'Untouchable', 'Sharp Mind'},
        "Dylan": {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer'}
        }
    list_sets = []
    #alice_set = set(players['Alice'])
    #print(alice_set)
    for name in players:
        print(f"Player: {name}", players[name])
        list_sets.append(set(players[name]))
    for sets in list_sets:
        print(f"sets: {sets}")


    result = distinct(list_sets)
    print(f"union {result}")
    print(f"intersection {intersection(list_sets)}")
    print(f"difference: {unique(players['Alice'], list_sets)}")
    print(f"difference charlie: {unique(players['Charlie'], list_sets)}")

