# Python Modules

Welcome to the **Python Modules** repository — a comprehensive collection of Python exercises structured into modules, designed to practice and master different concepts of the language, from the basics to advanced OOP, functional programming, error handling, and package management.

## 📦 Module Contents

| M. | Exercises | Key Concepts |
| :----: | --------- | ------------ |
| [00](module_00)<br><sub>*Python fundamentals with a garden theme*</sub> | [ex0](module_00/ex0/ft_hello_garden.py) · [ex1](module_00/ex1/ft_garden_name.py) · [ex2](module_00/ex2/ft_plot_area.py) · [ex3](module_00/ex3/ft_harvest_total.py) | `print()` · `input()` · type casting · string formatting |
|  | [ex4](module_00/ex4/ft_plant_age.py) · [ex5](module_00/ex5/ft_water_reminder.py) · [ex6](module_00/ex6/ft_count_harvest_iterative.py) · [ex7](module_00/ex7/ft_seed_inventory.py) | `if`/`elif`/`else` · `for`/`while` · iterative vs recursive logic |
| [01](module_01)<br><sub>*Modeling real-world entities with OOP*</sub> | [ex0](module_01/ex0/ft_garden_intro.py) · [ex1](module_01/ex1/ft_garden_data.py) · [ex2](module_01/ex2/ft_plant_growth.py) · [ex3](module_01/ex3/ft_plant_factory.py) · [ex4](module_01/ex4/ft_garden_security.py) | classes · `__init__` · instance vs class attributes · encapsulation |
|  | [ex5](module_01/ex5/ft_plant_types.py) · [ex6](module_01/ex6/ft_garden_analytics.py) | inheritance · `super()` · `@staticmethod` · `@classmethod` |
| [02](module_02)<br><sub>*Building resilient, crash-proof scripts*</sub> | [ex0](module_02/ex0/ft_first_exception.py) · [ex1](module_02/ex1/ft_raise_exception.py) · [ex2](module_02/ex2/ft_different_errors.py) | `try`/`except`/`else` · `raise` · `TypeError` · `ValueError` · `KeyError` |
|  | [ex3](module_02/ex3/ft_custom_errors.py) · [ex4](module_02/ex4/ft_finally_block.py) | custom exception classes · `finally` · exception chaining |
| [03](module_03)<br><sub>*CLI tools, collections, generators & comprehensions*</sub> | [ex0](module_03/ex0/ft_command_quest.py) | `sys.argv` · `argparse` · CLI argument parsing |
|  | [ex1](module_03/ex1/ft_score_analytics.py) · [ex2](module_03/ex2/ft_coordinate_system.py) · [ex3](module_03/ex3/ft_achievement_tracker.py) · [ex4](module_03/ex4/ft_inventory_system.py) | `list` · `tuple` · `set` · `dict` · mutability & ordering |
|  | [ex5](module_03/ex5/ft_data_stream.py) | generators · `yield` · lazy evaluation · `next()` |
|  | [ex6](module_03/ex6/ft_data_alchemist.py) | list/dict/set comprehensions · conditional expressions |
| [04](module_04)<br><sub>*Persisting data safely with files & context managers*</sub> | [ex0](module_04/ex0/ft_ancient_text.py) · [ex1](module_04/ex1/ft_archive_creation.py) · [ex2](module_04/ex2/ft_stream_management.py) | `open()` · `read()` · `write()` · file modes (`r`, `w`, `a`) |
|  | [ex3](module_04/ex3/ft_vault_security.py) | `with` statement · context managers · `__enter__`/`__exit__` |
| [05](module_05)<br><sub>*ETL-style pipelines via abstract & polymorphic components*</sub> | [ex0](module_05/ex0/data_processor.py) · [ex1](module_05/ex1/data_stream.py) · [ex2](module_05/ex2/data_pipeline.py) | `ABC` · `@abstractmethod` · polymorphism · method overriding · duck typing |
| [06](module_06)<br><sub>*Structuring codebases with packages & imports*</sub> | [al0](module_06/ft_alembic_0.py) · [al1](module_06/ft_alembic_1.py) · [al2](module_06/ft_alembic_2.py) · [al3](module_06/ft_alembic_3.py) · [al4](module_06/ft_alembic_4.py) · [al5](module_06/ft_alembic_5.py) | import mechanics · `__init__.py` · relative vs absolute imports |
|  | [di0](module_06/ft_distillation_0.py) · [di1](module_06/ft_distillation_1.py) · [tr0](module_06/ft_transmutation_0.py) · [tr1](module_06/ft_transmutation_1.py) · [tr2](module_06/ft_transmutation_2.py) | `from x import y` · `import as` · module aliasing · `__all__` |
|  | [kb0](module_06/ft_kaboom_0.py) · [kb1](module_06/ft_kaboom_1.py) | circular imports · `ImportError` · import order & side effects |
| [07](module_07)<br><sub>*Advanced OOP via a battle & tournament simulation*</sub> | [ex0](module_07/battle.py) · [ex1](module_07/capacitor.py) · [ex2](module_07/tournament.py) | factory pattern · abstract interfaces · strategy pattern · capability mixins |
| [08](module_08)<br><sub>*The professional Python toolchain — Matrix theme*</sub> | [ex0](module_08/ex0/construct.py) | `venv` · `sys.prefix` · `site-packages` · environment isolation |
|  | [ex1](module_08/ex1/loading.py) | `pip` · `poetry` · `requirements.txt` · `pyproject.toml` · `pandas` · `numpy` · `matplotlib` |
|  | [ex2](module_08/ex2/oracle.py) | `python-dotenv` · `.env` files · secrets management · config validation |
| [09](module_09)<br><sub>*Declarative data modeling & runtime validation — Space theme*</sub> | [ex0](module_09/ex0/space_station.py) · [ex1](module_09/ex1/alien_contact.py) · [ex2](module_09/ex2/space_crew.py) | `BaseModel` · `Field` · type coercion · `@validator` · `model_validator` · runtime safety |
| [10](module_10)<br><sub>*The functional side of Python*</sub> | [ex0](module_10/ex0/lambda_spells.py) | `lambda` · anonymous functions · inline expressions |
|  | [ex1](module_10/ex1/higher_magic.py) | `map()` · `filter()` · `sorted()` · `key=` · higher-order functions |
|  | [ex2](module_10/ex2/scope_mysteries.py) | LEGB scope · closures · `nonlocal` · mutable state in closures |
|  | [ex3](module_10/ex3/functools_artifacts.py) | `reduce` · `partial` · `lru_cache` · `singledispatch` · memoization |
|  | [ex4](module_10/ex4/decorator_mastery.py) | decorators · decorator factories · `functools.wraps` · `*args/**kwargs` preservation |

## 🚀 Getting Started

Clone the repository to explore and run the exercises locally:

```bash
git clone https://github.com/CarlosJX7/Python_Modules.git
cd Python_Modules
```

## 🔍 Code Quality & Standards

All exercises strictly adhere to **42 School** standards, ensuring clean architecture, PEP 8 compliance, and robust type safety:

- **`flake8`** — Linter enforcing PEP 8 style guides and identifying common code issues.
- **`mypy` (`--strict`)** — Static type analyzer ensuring comprehensive type annotation coverage.

### Installation

```bash
python3 -m pip install flake8 mypy
```

### Running Checks

Execute the checks within any module or exercise directory:

```bash
# Style & syntax check
python3 -m flake8

# Strict static type verification
python3 -m mypy --strict .
```

---

> 💡 **Requirement:** A Python 3.10+ environment is recommended to run and test all modules.
