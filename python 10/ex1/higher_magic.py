from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def get_power_str(target: str, power: int) -> str:
    return str(power)


def is_high_power(target: str, power: int) -> bool:
    return power > 50


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    amplified_spell = power_amplifier(get_power_str, 3)
    orig = get_power_str("Dummy", 10)
    amp = amplified_spell("Dummy", 10)
    print(f"Original: {orig}, Amplified: {amp}")

    cond_spell = conditional_caster(is_high_power, fireball)
    cond_spell("Goblin", 20)

    seq_spell = spell_sequence([fireball, heal])
    seq_spell("Orc", 15)


if __name__ == "__main__":
    main()
