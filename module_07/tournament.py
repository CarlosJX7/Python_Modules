from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    total = len(opponents)
    print(f"{total} opponents involved")
    for i in range(total):
        fact = opponents[i][0]
        strat = opponents[i][1]
        for j in range(i + 1, total):
            fact2, strat2 = opponents[j]
            creature1 = fact.create_base()
            creature2 = fact2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                strat.act(creature1)
                strat2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (heal, defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (heal, defensive)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua, normal),
        (heal, defensive),
        (transform, aggressive)
    ])
