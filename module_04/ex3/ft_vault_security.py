def secure_archive(filename: str, action: str, content: str = "Default") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as file:
                return True, file.read()
        if action == "w":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        return (False, "Unknown action")
    except OSError as e:
        return (False, str(e))



if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive("/not/existing/file", "r")
    print(f'({result[0]}, "{result[1]}")')
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result: tuple[bool, str] = secure_archive("inaccessible", "r")
    print(f'({result[0]}, "{result[1]}")')
    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt", "r")
    print(f'({result[0]}, "{result[1]}")')
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt", "w", "Nuevo texto")
    print(f'({result[0]}, "{result[1]}")')