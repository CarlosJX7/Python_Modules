from grimoire import light_spellbook


def  validate_ingredients(ingredients: str) -> str:
    ingred_list: str = ""
    valid: bool = False
    for spell in light_spellbook.light_spell_allowed_ingredients():
        if spell in ingredients.split(","):
            valid = True
            return ingredients + " - VALID"
    return ingredients + " - INVALID"

print(validate_ingredients("hola"))