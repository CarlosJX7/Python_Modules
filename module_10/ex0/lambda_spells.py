from lambda_spells import FuncMageDataGenerator

def artifact_sorter(
        artifacts: list[dict[str, str | int]]
        ) -> list[dict[str, str | int]]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    value: dict = {}
    max_power_mage = max(mages, key=lambda m: m["power"])
    value["max_power"] = max_power_mage["power"]
    return value


if __name__ == "__main__":
    artifacts = [{'name': 'Crystal Orb', 'power': 117, 'type': 'armor'}, {'name': 'Water Chalice', 'power': 89, 'type': 'relic'}, {'name': 'Lightning Rod', 'power': 104, 'type': 'focus'}, {'name': 'Wind Cloak', 'power': 67, 'type': 'weapon'}]

    spells = [
        "fuego",
        "hielo",
        "agua"
    ]
    nueva_lista = artifact_sorter(artifacts)
    print(nueva_lista)
    generator = FuncMageDataGenerator
    #magos_power = power_filter(artifacts, 3)
    #print(magos_power)
    #print(spell_transformer(spells))
    #print(mage_stats(artifacts))

