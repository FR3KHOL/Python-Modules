def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()

    for item in allowed:
        if item.lower() in ingredients.lower():
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
