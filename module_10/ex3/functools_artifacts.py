from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    match operation:
        case "add":
            return reduce(operator.add, spells)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return max(spells)
        case "min":
            return min(spells)
        case _:
            raise ValueError(f"Operation {operation} not found")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> dict[str, Callable]:
    """ Take a base enchantment function with signature (power: int, element: str, target:
        str)-> str
    """
    enchantments = {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "water": partial(base_enchantment, 50, "water")
    }
    return enchantments


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    @lru_cache(maxsize=None) guarda (memoiza) resultados de una función según
    los argumentos con los que fue llamada.

    Regla general:
    - Primera vez con ciertos argumentos: la función se ejecuta y el resultado
    se almacena en caché.
    - Siguientes veces con esos mismos argumentos: se devuelve el resultado
    almacenado, sin volver a ejecutar el cuerpo de la función.

    Beneficio:
    - Evita cálculos repetidos y mejora el rendimiento en llamadas frecuentes
    con entradas iguales.

    Notas:
    - Si los argumentos cambian, se calcula de nuevo.
    - Los argumentos deben ser hashables.
    - cache_info() muestra estadísticas de uso de caché.
    - cache_clear() limpia la caché.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """
    `singledispatch` works like a type-based switch/case.

    - The function decorated with `@singledispatch` is the generic entry point
    and acts as the default/fallback case.
    - `@<dispatcher>.register` adds specialized handlers for concrete types
    (e.g., int, str, list).
    - At call time, the dispatcher inspects the first argument's runtime type
    and routes execution to the best matching registered handler.
    - You can register multiple handlers for one dispatcher.
    - Dispatcher names are not special (`dispatch_spell`, `cast`, etc.):
    it is just the function name bound to the singledispatch object.
    """
    @singledispatch
    def dispatcher(spell: Any) -> str:
            return F"Type not found {type(spell)}"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"[int] Damage spell {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"[str] Enchantment {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"[list] Multicast: {len(spell)} spells"

    return dispatcher

def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Element: {element} with {power} and targeting ---> {target} <---"


if __name__ == "__main__":
    suma = [10, 42]
    res = spell_reducer(suma, "max")
    print(res)
    print(base_enchantment(42, "earth", "orc"))
    part_ench = partial_enchanter(base_enchantment)
    fire_ench = part_ench["fire"]
    print(fire_ench("mage"))

    func_dispatch = spell_dispatcher()
    print(func_dispatch(42))
    print(func_dispatch("42"))
    print(func_dispatch(func_dispatch))
    print(func_dispatch([42, "43"]))
