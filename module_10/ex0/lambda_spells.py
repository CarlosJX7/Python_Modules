from collections.abc import Callable
from typing import Any

def suma(a: int):
    return a + 1


def par(b: int):
    return b % 2

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    value: dict = {}
    max_power_mage = max(mages, key=lambda m: m["power"])
    value["max_power"] = max_power_mage["power"]
    return value

if __name__ == "__main__":
    numeros = [1, 2, 42, 3]
    resultado = map(suma, numeros)
    print(list(resultado))
    filtro = filter(par, numeros)
    print(list(filtro))
    ordenado = sorted(numeros, reverse=True)
    print(ordenado)

    lista = [
        {"nombre": "uno", "power": 1},
        {"nombre": "tres", "power": 3},
        {"nombre": "dos", "power": 2}
    ]


    spells = [
        "fuego",
        "hielo",
        "agua"
    ]
    nueva_lista = artifact_sorter(lista)
    print(nueva_lista)
    magos_power = power_filter(lista, 3)
    print(magos_power)
    print(spell_transformer(spells))
    print(mage_stats(lista))