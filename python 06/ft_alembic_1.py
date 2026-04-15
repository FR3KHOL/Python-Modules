from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    s = "Using: 'from ... import ...' structure to access elements.py"
    print(s)
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
