from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def valid_power(target: str, power: int) -> bool:
    return power > 0


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
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
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
    print("===== Spell combiner =====")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon", 42)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\n===== Power amplifier =====")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original  : {fireball('goblin', 10)}")
    print(f"Amplified : {mega_fireball('goblin', 10)}")

    print("\n===== Conditional caster =====")
    cond_spell = conditional_caster(valid_power, fireball)
    print(cond_spell("wizard", 15))
    print(cond_spell("wizard", -5))

    print("\n===== Spell sequence =====")
    spells_list: list[Callable[[str, int], str]] = [fireball, heal]
    seq_spells = spell_sequence(spells_list)
    print(seq_spells("mage", 11))

    print("\n===== callable() demo =====")
    print(f"fireball is callable  : {callable(fireball)}")
    print(f"heal is callable      : {callable(heal)}")
    print(f"42 is callable        : {callable(42)}")
    print(f"combined_spell is callable: {callable(combined_spell)}")
