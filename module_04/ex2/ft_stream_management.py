import sys
import typing


def save_text(text: str) -> None:
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    file_name = sys.stdin.readline().rstrip("\n")
    if file_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to: '{file_name}'")
    try:
        new_file = open(file_name, "w")
        new_file.write(text)
        new_file.close()
        print(f"Data saved in {file_name}")
    except OSError as e:
        sys.stderr.write(
                        f"[STDERR] Error opening file '{file_name}':"
                        f" {e}\n Data not saved.\n"
                        )


def format_text(text: str) -> str:
    new_text = ""

    for char in text:
        if char == "\n":
            char = "#\n"
        new_text = new_text + char

    if new_text != "" and new_text[-1] != "\n":
        new_text = new_text + "#"

    return new_text


def get_content(fd: typing.IO[str]) -> str:
    text = fd.read()
    return text


def data_recover() -> str | None:
    file = sys.argv[1]
    try:
        print(f"Accessing file '{file}'\n---")
        fd = open(file)
        new_text = get_content(fd)
        print(new_text, end="")
        fd.close()
        print(f"\n---\nFile '{file}' closed.")
        return new_text
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}\n")
        return None


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    text = data_recover()
    if text is None:
        return
    print("\nTransform data: \n---")
    new_text = format_text(text)
    print(new_text, "\n---")
    save_text(new_text)


if __name__ == "__main__":
    main()
