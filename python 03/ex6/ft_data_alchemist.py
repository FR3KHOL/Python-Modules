import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    cap_all = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {cap_all}")
    cap_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {cap_only}")

    scores_dict = {name: random.randint(0, 1000) for name in cap_all}
    print(f"Score dict: {scores_dict}")

    average = round(sum(scores_dict.values()) / len(scores_dict), 2)
    print(f"Score average is {average}")
    high_scores = {k: v for k, v in scores_dict.items() if v > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
