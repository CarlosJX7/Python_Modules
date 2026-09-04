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
    from data_generator import FuncMageDataGenerator
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


