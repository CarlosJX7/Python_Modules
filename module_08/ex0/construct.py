import os
import site
import sys


def inside_env() -> bool:
    """Check if python is running inside a virtual environment."""
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def main() -> None:
    """Display environment status and matrix instructions."""
    if not inside_env():
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("Then run this program again.")
    else:
        env_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
