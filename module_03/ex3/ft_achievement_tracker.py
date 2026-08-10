import random


def gen_player_achievements() -> set[str]:
    p_achievements: set[str] = set()
    random_size = random.randint(1, len(achievements))
    while len(p_achievements) < random_size:
        random_index = random.randint(0, len(achievements) - 1)
        p_achievements = p_achievements.union({achievements[random_index]})
    return p_achievements


def distinct(data: list[set[str]]) -> set[str]:
    items: set[str] = set()
    for d in data:
        items = items.union(d)
    return items


def intersection(data: list[set[str]]) -> set[str]:
    return set.intersection(*data)


def unique(player_name: str, players: dict[str, set[str]]) -> set[str]:
    others: set[str] = set()
    for name in players:
        if name != player_name:
            others = others.union(players[name])
    return players[player_name].difference(others)


def missing(player_data: set[str], data: list[str]) -> set[str]:
    return set(data).difference(player_data)


def get_example() -> dict[str, set[str]]:
    players: dict[str, set[str]] = {
        "Alice": {
            "Crafting Genius",
            "World Savior",
            "Master Explorer",
            "Collector Supreme",
            "Untouchable",
            "Boss Slayer",
        },
        "Bob": {
            "Crafting Genius",
            "Strategist",
            "World Savior",
            "Master Explorer",
            "Unstoppable",
            "Collector Supreme",
            "Untouchable",
        },
        "Charlie": {
            "Strategist",
            "Speed Runner",
            "Survivor",
            "Master Explorer",
            "Treasure Hunter",
            "First Steps",
            "Collector Supreme",
            "Untouchable",
            "Sharp Mind",
        },
        "Dylan": {
            "Strategist",
            "Speed Runner",
            "Unstoppable",
            "Untouchable",
            "Boss Slayer",
        },
    }
    return players


def get_list(data: dict[str, set[str]]) -> list[set[str]]:
    p_list: list[set[str]] = []
    for d in data:
        p_list.append(data[d])
    return p_list


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
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
    players = get_example()
    # players = {
    #             "Alice" : gen_player_achievements(),
    #             "Bob" : gen_player_achievements(),
    #             "Charlie" : gen_player_achievements(),
    #             "Dylan" : gen_player_achievements()
    #             }

    for p in players:
        print(f"Player {p}: {players[p]}")
    list_sets = get_list(players)
    print(f"\nAll distinct achivements: {distinct(list_sets)}")
    print(f"\nCommon achievements: {intersection(list_sets)}\n")

    for p in players:
        print(f"Only {p} has {unique(p, players)}")
    print()
    for p in players:
        print(f"{p} is missing: {missing(players[p], achievements)}")
