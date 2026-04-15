from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    ans = transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {ans}")


if __name__ == "__main__":
    main()
