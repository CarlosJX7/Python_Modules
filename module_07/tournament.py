from ex2.strategies import NormalStrategy
from ex2.strategies import AggressiveStrategy, DefensiveStrategy
import ex1
import ex0

factory = ex0.FlameFactory()
crature = factory.create_base()
strat = NormalStrategy()
strat.act(crature)
print("re")
factory_tr = ex1.TransformCreatureFactory()
creature_ag = factory_tr.create_base()
strat = AggressiveStrategy()
strat.act(creature_ag)

factory_heal = ex1.HealingCreatureFactory()
creature_heal = factory_heal.create_base()
strat = DefensiveStrategy()
strat.act(creature_heal)
