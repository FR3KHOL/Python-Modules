import sys


def main() -> None:
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")

    args_num_total = len(sys.argv)
    args_num = args_num_total - 1

    if args_num == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args_num}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {args_num_total}")


if __name__ == "__main__":
    main()
