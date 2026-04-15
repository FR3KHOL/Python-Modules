from ..elements import create_air
from alchemy.potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    fire = create_fire()
    s = f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' "
    s += f"mixed with '{fire}'"
    return s
