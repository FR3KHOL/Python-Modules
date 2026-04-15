from alchemy import grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ans = grimoire.light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {ans}")


if __name__ == "__main__":
    main()
