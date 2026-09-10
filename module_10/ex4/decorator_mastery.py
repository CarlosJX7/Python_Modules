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
    pass


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball!"

if __name__ == "__main__":
    print(fireball())