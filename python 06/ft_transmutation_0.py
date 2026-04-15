import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    ans = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {ans}")


if __name__ == "__main__":
    main()
