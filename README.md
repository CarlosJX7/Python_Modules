# Python Modules

Welcome to the **Python Modules** repository. This project is a comprehensive collection of Python exercises structured into several modules. It is designed to practice and master different concepts of Python programming, from the basics to advanced Object-Oriented Programming (OOP), error handling, and package management.

## 📁 Repository Structure

### Module 00: Basics (Garden Theme)
**Description:** An introduction to Python fundamentals using a garden-themed set of exercises.  
**What you learn:** Basic syntax, variables, standard data types, simple arithmetic operations, control flow, loops, and the difference between iterative and recursive functions.  
**Utility:** Establishes the foundational knowledge required to write functional Python scripts and understand the core mechanics of the language.

- `ex0`: `ft_hello_garden.py`
- `ex1`: `ft_garden_name.py`
- `ex2`: `ft_plot_area.py`
- `ex3`: `ft_harvest_total.py`
- `ex4`: `ft_plant_age.py`
- `ex5`: `ft_water_reminder.py`
- `ex6`: `ft_count_harvest_iterative.py`, `ft_count_harvest_recursive.py`
- `ex7`: `ft_seed_inventory.py`

### Module 01: Object-Oriented Programming Introduction
**Description:** A deep dive into the paradigm of Object-Oriented Programming (OOP) in Python.  
**What you learn:** Classes, objects, instantiation, methods, instance and class attributes, and basic encapsulation.  
**Utility:** Enables the creation of modular, organized code that models real-world entities, making large codebases easier to maintain and scale.

- `ex0`: `ft_garden_intro.py`
- `ex1`: `ft_garden_data.py`
- `ex2`: `ft_plant_growth.py`
- `ex3`: `ft_plant_factory.py`
- `ex4`: `ft_garden_security.py`
- `ex5`: `ft_plant_types.py`
- `ex6`: `ft_garden_analytics.py`

### Module 02: Exceptions and Error Handling
**Description:** Focuses on making scripts robust and preventing unexpected crashes.  
**What you learn:** Using `try`, `except`, `raise`, `finally` blocks, and creating custom exception classes to handle edge cases gracefully.  
**Utility:** Essential for developing resilient applications that can handle bad input, network failures, or missing files without breaking.

- `ex0`: `ft_first_exception.py`
- `ex1`: `ft_raise_exception.py`
- `ex2`: `ft_different_errors.py`
- `ex3`: `ft_custom_errors.py`
- `ex4`: `ft_finally_block.py`

### Module 03: System and Data Streams
**Description:** Teaches how to interact with the environment and process linear streams of data.  
**What you learn:** Command-line argument parsing, basic I/O operations, coordinating multiple data inputs, and tracking states like scores and inventories.  
**Utility:** Provides the necessary skills to build command-line tools and interact seamlessly with system resources and user inputs.

- `ex0`: `ft_command_quest.py`
- `ex1`: `ft_score_analytics.py`
- `ex2`: `ft_coordinate_system.py`
- `ex3`: `ft_achievement_tracker.py`
- `ex4`: `ft_inventory_system.py`
- `ex5`: `ft_data_stream.py`
- `ex6`: `ft_data_alchemist.py`

### Module 04: Archives and Vault Security
**Description:** Exercises focused on file management and data persistence.  
**What you learn:** Reading and writing files, creating archives, managing data streams over time, and basic security concepts for safe data storage.  
**Utility:** Crucial for applications that need to save user state, logs, or any information that must persist beyond a single session.

- `ex0`: `ft_ancient_text.py`
- `ex1`: `ft_archive_creation.py`
- `ex2`: `ft_stream_management.py`
- `ex3`: `ft_vault_security.py`

### Module 05: Data Processing Pipelines
**Description:** Introduces the concept of data engineering on a micro scale.  
**What you learn:** Processing large chunks of data sequentially, filtering, transforming data, and building functional pipelines.  
**Utility:** Highly useful for data science, ETL (Extract, Transform, Load) tasks, and processing logs efficiently.

- `ex0`: `data_processor.py`
- `ex1`: `data_stream.py`
- `ex2`: `data_pipeline.py`

### Module 06: Alchemy (Modules and Packages)
**Description:** Covers the structure and organization of professional Python codebases.  
**What you learn:** Creating Python packages, using `__init__.py`, organizing sub-packages, and importing internal/external modules securely.  
**Utility:** Teaches how to structure large applications into reusable components, which is standard practice in real-world software engineering.

- `alchemy/`: A package simulating alchemy with elements, potions, and grimoires.
  - `grimoire/`: Sub-package containing light and dark spellbooks and validators.
  - `transmutation/`: Sub-package containing recipes.
- `elements.py`
- **Alembic Scripts**: `ft_alembic_0.py` to `ft_alembic_5.py`
- **Distillation Scripts**: `ft_distillation_0.py`, `ft_distillation_1.py`
- **Kaboom Scripts**: `ft_kaboom_0.py`, `ft_kaboom_1.py`
- **Transmutation Scripts**: `ft_transmutation_0.py`, `ft_transmutation_1.py`, `ft_transmutation_2.py`

### Module 07: Advanced OOP and Battle System
**Description:** Applies advanced OOP concepts through the creation of a modular battle and tournament simulation.  
**What you learn:** Abstract base classes, inheritance, polymorphism, factory design pattern, composition, capability mixins/interfaces, and strategy patterns for dynamic behaviors and combat rules.  
**Utility:** Builds architectural thinking skills required for designing scalable, maintainable systems such as game engines, simulation tools, UI frameworks, or backend business logic.

- **Simulation Runners**:
  - `battle.py`: Basic battle and creature factory demonstration (`FlameFactory`, `AquaFactory`).
  - `capacitor.py`: Capability and evolution tests (healing and transformation mechanics).
  - `tournament.py`: Strategy-driven tournament engine with error handling for invalid moves.
- **Packages & Modules**:
  - `ex0`: Base creature hierarchy and abstract creature factories (`creature.py`, `creature_factory.py`, `aqua_family.py`, `flame_family.py`).
  - `ex1`: Capability interfaces, healing capabilities, and dynamic transformation behaviors (`capabilities.py`, `healing_family.py`, `transform_family.py`).
  - `ex2`: Pluggable battle strategies (normal, aggressive, defensive) and custom strategy error handling (`strategies.py`).

### Module 08: Environments, Packages, and Configuration (Matrix Theme)
**Description:** Focuses on Python development environments, dependency management, package managers, and secure configuration handling using a Matrix-inspired theme.  
**What you learn:** Virtual environment detection and isolation (`sys.prefix`, `site`), dependency declaration and management (`requirements.txt`, `pyproject.toml` with Poetry), third-party data processing & visualization libraries (`pandas`, `numpy`, `matplotlib`), and secure environment variable handling with `python-dotenv`.  
**Utility:** Fundamental for professional software development, reproducibility across machines, securing sensitive credentials, and cleanly managing project dependencies.

- `ex0`: `construct.py` - Virtual environment detector and isolation validator.
- `ex1`: `loading.py`, `requirements.txt`, `pyproject.toml` - Runtime dependency inspection, synthetic data generation with NumPy/Pandas, and histogram plotting with Matplotlib (`matrix_analysis.png`).
- `ex2`: `oracle.py`, `.env.example`, `.gitignore`, `requirements.txt` - Environment configuration loader (`python-dotenv`), sensitive value masking, and environment security validation.

## 🚀 Getting Started

Clone the repository and explore each module's directory. Each module contains specific exercises that build upon each other.

```bash
git clone https://github.com/CarlosJX7/Python_Modules.git
cd Python_Modules
```

---
*Note: Make sure you have a working Python environment (version 3.x recommended) to run the scripts.*
