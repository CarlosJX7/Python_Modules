import alchemy
from elements import create_fire
from ..elements import create_air


def lead_to_gold() -> str:
    return (
            f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{alchemy.potions.strength_potion()}' "
            f"mixed with '{create_fire()}'"
            )
