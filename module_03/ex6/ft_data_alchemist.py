import random


def random_number() -> int:
    return random.randint(0, 1000)


def get_total(scores: dict[str, int]) -> int:
    total = 0
    for name in scores:
        total += scores[name]
    return total


if __name__ == "__main__":
    list_players = [
                    'Alice',
                    'bob',
                    'Charlie',
                    'dylan',
                    'Emma',
                    'Gregory',
                    'john',
                    'kevin',
                    'Liam'
                    ]
    cap_players = [name.capitalize() for name in list_players]
    only_cap = [name for name in list_players if name == name.capitalize()]
    print(f"Inicial list of players: {list_players}")
    print(f"New list with all names capitalized:    {cap_players}")
    print(f"New list of capitalized names only: {only_cap}")
    scores: dict[str, int] = {name: random_number() for name in only_cap}
    print(f"Score dict {scores}")
    average = get_total(scores) / len(only_cap)
    print(f"Score average: {average}")
    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
        }
    print(high_scores)
