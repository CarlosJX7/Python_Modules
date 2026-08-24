import ex1


def transform_test(factory: ex1.TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    print("base:")
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def healing_test(factory: ex1.HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")

    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


if __name__ == "__main__":
    heal_factory = ex1.HealingCreatureFactory()
    healing_test(heal_factory)
    transform_factory = ex1.TransformCreatureFactory()
    transform_test(transform_factory)
