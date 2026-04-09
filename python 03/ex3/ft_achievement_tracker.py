import random

MASTER_BADGES = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    unlock_count = random.randint(5, 9)
    random_picks = random.sample(MASTER_BADGES, unlock_count)

    return set(random_picks)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice_set = gen_player_achievements()
    bob_set = gen_player_achievements()
    charlie_set = gen_player_achievements()
    dylan_set = gen_player_achievements()

    gamer_profiles = [
        ("Alice", alice_set),
        ("Bob", bob_set),
        ("Charlie", charlie_set),
        ("Dylan", dylan_set)
    ]

    for gamer_name, badges in gamer_profiles:
        print(f"Player {gamer_name}: {badges}")

    global_unique = alice_set.union(bob_set, charlie_set, dylan_set)
    print(f"\nAll distinct achievements: {global_unique}")

    shared_by_all = alice_set.intersection(bob_set, charlie_set, dylan_set)
    print(f"\nCommon achievements: {shared_by_all}\n")

    for target_name, target_badges in gamer_profiles:
        rivals_badges: set[str] = set()

        for rival_name, rival_badges in gamer_profiles:
            if target_name != rival_name:
                rivals_badges = rivals_badges.union(rival_badges)

        exclusive_to_gamer = target_badges.difference(rivals_badges)
        print(f"Only {target_name} has: {exclusive_to_gamer}")

    complete_collection = set(MASTER_BADGES)
    print()
    for gamer_name, badges in gamer_profiles:
        yet_to_unlock = complete_collection.difference(badges)
        print(f"{gamer_name} is missing: {yet_to_unlock}")


if __name__ == "__main__":
    main()
