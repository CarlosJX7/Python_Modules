from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory


def test_battle(aqua: CreatureFactory, flame: CreatureFactory) -> None:
    print("Testing battle")

    base_flame = flame.create_base()
    base_aqua = aqua.create_base()

    print(base_flame.describe())
    print("vs.")
    print(base_aqua.describe())
    print("fight!")

    print(base_flame.attack())
    print(base_aqua.attack())


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack(), end="\n\n")


def main() -> None:
    flame_factory = FlameFactory()
    test_factory(flame_factory)
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)
    test_battle(aqua_factory, flame_factory)


if __name__ == "__main__":
    main()
