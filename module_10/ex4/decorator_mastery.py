from functools import wraps
from typing import Callable
import time


def spell_timer(func: Callable)-> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {func.__name__} ...")
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print(f"Spell completed in {elapsed_time: .3f} seconds")
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


class MagueGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        name_check =  len(name) >= 3
        char_check = True
        for char in name:
            if not char.isalpha() or not char.isspace():
                char_check = False
        return name_check and char_check


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
    print(fireball())
    print(unstable_spell())