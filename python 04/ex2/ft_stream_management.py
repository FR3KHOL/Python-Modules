import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_stream_management.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, 'r')
        content = file.read()
        print(content, end="")
        if content and not content.endswith('\n'):
            print()
        file.close()
        print(f"File '{filename}' closed.")

        print("Transform data:")
        transformed_lines = []
        for line in content.splitlines():
            new_line = f"{line}#"
            transformed_lines.append(new_line)
            print(new_line)

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        new_file = sys.stdin.readline()
        if new_file.endswith('\n'):
            new_file = new_file[:-1]

        if not new_file:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            try:
                out_file = open(new_file, 'w')
                for line in transformed_lines:
                    out_file.write(f"{line}\n")
                out_file.close()
                print(f"Data saved in file '{new_file}'.")
            except Exception as e:
                print(f"[STDERR] Error opening file '{new_file}': {e}",
                      file=sys.stderr)
                print("Data not saved.")

    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)


if __name__ == "__main__":
    main()
