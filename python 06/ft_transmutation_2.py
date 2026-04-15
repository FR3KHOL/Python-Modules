import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    ans = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {ans}")


if __name__ == "__main__":
    main()
