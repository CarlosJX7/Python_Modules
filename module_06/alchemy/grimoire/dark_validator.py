from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    allowed = [spell.lower() for spell in allowed]
    ingredients_list = ingredients.split(",")
    ingredients_list = [ing.lower() for ing in ingredients_list]
    ingredients_list = [ing.strip() for ing in ingredients_list]
    valid = any(item in allowed for item in ingredients_list)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
