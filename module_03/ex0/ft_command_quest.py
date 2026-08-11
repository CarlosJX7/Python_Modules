import sys


def print_arguments(argv: list[str]) -> None:
    print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    argv = sys.argv
    total = len(argv)
    print(f"Program name: {argv[0]}")
    if total == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
    i = 0
    while i < total:
        if argv[i] != sys.argv[0]:
            print(f"Argument {i}: {argv[i]}")
        i += 1
    print_arguments(argv)
