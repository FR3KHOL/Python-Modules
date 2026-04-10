import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, 'r')
        data = file.read()

        print(data, end="")

        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("Transform data:")
    lines = data.splitlines()
    transformed_lines = [line + "#" for line in lines]

    for line in transformed_lines:
        print(line)

    new_file = input("Enter new file name (or empty): ")

    if new_file:
        print(f"Saving data to '{new_file}'")
        try:
            out_file = open(new_file, 'w')
            for line in transformed_lines:
                out_file.write(line + "\n")
            out_file.close()
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"Error opening file '{new_file}': {e}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
