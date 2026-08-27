import os
import sys
import site

def inside_env() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)

if __name__ == "__main__":
    if not inside_env():
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
    else:
        env_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(site.getsitepackages()[0])
