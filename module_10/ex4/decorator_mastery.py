from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable)-> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {func.__name__} ...")
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int)-> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None:
                if len(args) >= 3:
                    power = args[2]
                if len(args) == 2:
                    power = args[1]

            if power is None or power < min_power:
                return "Insufficient power for this spell"
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



def retry_spell(max_attempts: int)-> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if attempt < max_attempts:
                         print(
                            f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        is_valid_char = lambda c: c.isalpha() or c.isspace()
        char_validity = map(is_valid_char, name)
        return all(char_validity)


    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"



@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball!"


@retry_spell(3)
def unstable_spell() -> str:
    raise RuntimeError("failed")

if __name__ == "__main__":
    print("===== Spell timer =====")
    print(fireball())

    print("\n===== Retry spell =====")
    print(unstable_spell())

    print("\n===== Waaaagh spelled! =====")

    @retry_spell(3)
    @spell_timer
    def waaagh() -> str:
        return "Waaaaaaagh spelled !"

    print(waaagh())

    print("\n===== MageGuild =====")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))