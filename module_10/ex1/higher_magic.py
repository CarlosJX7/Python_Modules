from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def valid_power(power: int) -> bool:
    if power > 0:
        return True
    return False


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combiner(target: str, power: int) -> tuple[str, str]:
        first_spell = spell1(target, power)
        second_spell = spell2(target, power)
        return (first_spell, second_spell)
    return combiner


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        power = power * multiplier
        return base_spell(target, power)
    return amplified


def conditional_caster(
        condition: Callable[[int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        status = condition(power)
        if status:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        spell_list = []
        for spell in spells:
            spell_list.append(spell(target, power))
        return spell_list
    return sequence


if __name__ == "__main__":
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("dragon", 42))
    base_spell = fireball
    multiplied_spell = power_amplifier(base_spell, 10)
    print(base_spell("goblin", 2))
    print(multiplied_spell("goblin", 2))
    cond_func = conditional_caster(valid_power, fireball)
    print(cond_func("wizard", 1))
    print(cond_func("wizard", -1))
    spells_list: list[Callable[[str, int], str]] = [fireball, heal]
    seq_spells = spell_sequence(spells_list)
    print(seq_spells("mage", 11))
