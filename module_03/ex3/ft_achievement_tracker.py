import random


def gen_player_achievements() -> set:
    p_achievements = set()
    random_size = random.randint(1, len(achievements))
    while len(p_achievements) < random_size:
        random_index = random.randint(0, len(achievements)- 1)
        p_achievements =  p_achievements.union({achievements[random_index]})
    return p_achievements


def distinct(data: list[set]) -> set:
        items = set()
        for d in data:
            items = items.union(d)
        return items


def intersection(data: list[set]) -> set:
    return set.intersection(*data)


def unique(player_data: set, data: list[set]) -> set:
    original_data = player_data
    for d in data:
        if d == original_data:
            continue
        player_data = player_data.difference(d)
    return player_data


def missing(player_data: set, data: list[str]) -> set:
    return set(achievements).difference(player_data)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievements = [
                    'Crafting Genius',
                    'World Savior',
                    'Master Explorer',
                    'Collector Supreme',
                    'Untouchable',
                    'Boss Slayer',
                    'Strategist',
                    'Unstoppable',
                    'Speed Runner',
                    'Survivor',
                    'Treasure Hunter',
                    'First Steps',
                    'Sharp Mind',
                    'Hidden Path Finder'
                    ]
    players = {
        "Alice": {'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer'},
        "Bob": {'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable'},
        "Charlie": {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'FirstSteps', 'Collector Supreme', 'Untouchable', 'Sharp Mind'},
        "Dylan": {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer'}
        }
    list_sets = []
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
    print(f"missing alice: {missing(players['Alice'], achievements)}")
    print(f"missing bob {missing(players['Bob'], achievements)}")
    print(f"missing charlie {missing(players['Charlie'], achievements)}")
    print(f"missing dylan {missing(players['Dylan'], achievements)}")
