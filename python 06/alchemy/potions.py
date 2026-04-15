import elements
from . import elements as alch_elements


def healing_potion() -> str:
    earth = alch_elements.create_earth()
    air = alch_elements.create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
