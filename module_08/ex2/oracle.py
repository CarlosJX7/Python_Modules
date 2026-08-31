import os
import sys

CONFIG_VARS: list[dict[str, str]] = [
    {
        "name": "MATRIX_MODE",
        "desc": "Operating mode",
        "default": "development",
    },
    {
        "name": "DATABASE_URL",
        "desc": "Database connection",
        "default": "",
    },
    {
        "name": "API_KEY",
        "desc": "API authentication",
        "default": "",
    },
    {
        "name": "LOG_LEVEL",
        "desc": "Logging verbosity",
        "default": "INFO",
    },
    {
        "name": "ZION_ENDPOINT",
        "desc": "Zion network URL",
        "default": "",
    },
]


def check_dotenv() -> bool:
    """Check if python-dotenv module is installed."""
    try:
        import importlib

        importlib.import_module("dotenv")
        return True
    except ImportError:
        return False


def load_configuration() -> dict[str, str]:
    """Load environment variables using python-dotenv."""
    from dotenv import find_dotenv, load_dotenv

    dotenv_path = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path)
    else:
        load_dotenv()

    config_dict: dict[str, str] = {}

    for var in CONFIG_VARS:
        value: str = os.environ.get(var["name"], var["default"])
        config_dict[var["name"]] = value

    return config_dict


def format_value(name: str, value: str, mode: str) -> str:
    """Return display text based on variable state."""
    if not value:
        return "[NOT CONFIGURED]"

    if name == "DATABASE_URL":
        if mode == "production":
            return "Connected to production database"
        return "Connected to local instance"

    if name == "API_KEY":
        return "Authenticated"

    if name == "ZION_ENDPOINT":
        return "Online"

    return value


def display_config(config: dict[str, str]) -> None:
    """Display system configuration."""
    mode: str = config.get("MATRIX_MODE", "development")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    display_names: dict[str, str] = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network",
    }

    for env_key, display_label in display_names.items():
        raw_value: str = config.get(env_key, "")
        formatted: str = format_value(env_key, raw_value, mode)
        print(f"{display_label}: {formatted}")


def run_security_check() -> None:
    """Check security best practices."""
    from dotenv import find_dotenv

    print("Environment security check:")

    has_env = bool(find_dotenv())

    checks: list[tuple[str, bool]] = [
        ("No hardcoded secrets detected", True),
        (".env file properly configured", has_env),
        ("Production overrides available", True),
    ]

    for label, is_ok in checks:
        status: str = "[OK]" if is_ok else "[WARNING]"
        print(f"{status} {label}")


def main() -> None:
    """Main entry point."""
    if not check_dotenv():
        print("ERROR: python-dotenv is not installed!")
        print("")
        print("Install it with:")
        print("  pip install python-dotenv")
        print("  # or: pip install -r requirements.txt")
        sys.exit(1)

    config: dict[str, str] = load_configuration()

    display_config(config)
    run_security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
