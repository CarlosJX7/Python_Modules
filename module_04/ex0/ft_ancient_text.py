import sys
import typing


def get_content(fd: typing.IO[str]) -> str:
    text = fd.read()
    return text


def data_recover() -> None:
    file = None
    try:
        file = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file}'")
        fd = open(file)
        print("---")
        print(get_content(fd), end="")
        fd.close()
        print(f"\n---\nFile '{file}' closed.")
    except OSError as e:
        print(f"Error opening file '{file}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    data_recover()


if __name__ == "__main__":
    main()
