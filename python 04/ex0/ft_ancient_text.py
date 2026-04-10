import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:

        file = open(filename, 'r')
        data = file.read()

        print(data, end="")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:

        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
