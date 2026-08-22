from .dark_validator import validate_ingredients

def  dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frog", "arsenic", "fireball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid_result = validate_ingredients(ingredients)
    if valid_result.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({valid_result})"
    return f"Spell rejected: {spell_name} ({valid_result})"
