def artifact_sorter(
        artifacts: list[dict[str, str | int]]
        ) -> list[dict[str, str | int]]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(
        mages: list[dict[str, int]],
        min_power: int
        ) -> list[dict[str, int]]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, int | float]]) -> dict[str, int | float]:
    value: dict[str, int | float] = {}
    value["max_power"] = max(mages, key=lambda m: m["power"])["power"]
    value["min_power"] = min(mages, key=lambda m: m["power"])["power"]
    value["avg_power"] = round(
        sum(map(lambda m: m["power"], mages)) / len(mages), 2
    )
    return value


if __name__ == "__main__":
    from data_generator import FuncMageDataGenerator  # type: ignore

    artifacts = FuncMageDataGenerator.generate_artifacts(4)
    s_artifacts = artifact_sorter(artifacts)
    print("===== Sorting artifacts ======")
    print("BEFORE:")
    for a in artifacts:
        print(f"{a['name']: <15} | {a['power']}")
    print("\nAFTER:")
    for a in s_artifacts:
        print(f"{a['name']: <15} | {a['power']}")

    print("\n===== Filtering mages =====")
    mages = FuncMageDataGenerator.generate_mages(4)
    f_mages = power_filter(mages, 100)
    for m in f_mages:
        print(f"{m['name']: <15} | {m['power']}")

    print("\n===== Spell transformer =====")
    spells = FuncMageDataGenerator.generate_spells(3)
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\n===== Mage stats =====")
    stats = mage_stats(mages)
    print(f"Max power : {stats['max_power']}")
    print(f"Min power : {stats['min_power']}")
    print(f"Avg power : {stats['avg_power']}")
