def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m.get('power', 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m.get('power', 0)).get('power', 0)
    min_p = min(mages, key=lambda m: m.get('power', 0)).get('power', 0)

    total = sum(map(lambda m: m.get('power', 0), mages))
    avg_p = round(total / len(mages), 2)

    return {'max_power': max_p, 'min_power': min_p, 'avg_power': avg_p}


def main() -> None:
    print("\nTesting artifact sorter..")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]

    sorted_arts = artifact_sorter(artifacts)
    if len(sorted_arts) >= 2:
        a1 = sorted_arts[0]
        a2 = sorted_arts[1]
        print(f"{a1['name']} ({a1['power']} power) comes before "
              f"{a2['name']} ({a2['power']} power)")

    print("\nTesting spell transformer....")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    for s in transformed:
        print(s, end=" ")


if __name__ == "__main__":
    main()
