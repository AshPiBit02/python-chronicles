# Python Chronicles

A hands-on Python learning repository that progresses from core language fundamentals to object-oriented programming, design patterns, and practical mini-projects.

## Repository structure

| Directory | Contents |
| --- | --- |
| [`01_basics`](01_basics) | Strings, containers, functions, modules, scope, file handling, exceptions, and small scripts such as a countdown timer. |
| [`02_intermediate`](02_intermediate) | Object-oriented programming, class mechanics, inheritance, composition, descriptors, properties, magic methods, context managers, and modules. |
| [`03_advanced`](03_advanced) | Design patterns including factory, builder, singleton, adapter, decorator, observer, and strategy patterns, plus advanced module examples. |
| [`04_projects`](04_projects) | Applied exercises built with OOP and design patterns, including banking, inventory, billing, e-commerce, file compression, financial reporting, notifications, and more. |

The repository also contains sample text, JSON, CSV, log, image, and PDF files used by file-handling and project exercises.

## Featured projects

Examples in `04_projects` include:

- Coffee Shop Billing System
- Car Rental System
- E-Commerce Shopping Cart Checkout System
- File Compression Tool
- Financial Report Generator
- Inventory System
- Loan EMI Calculator
- Notification System
- Online Learning Course System
- Stock Market Tracker
- Wi-Fi Router Manager

## Getting started

### Requirements

- Python 3.12 or newer is recommended.
- No third-party dependencies are required for the examples currently in the repository.

### Clone the repository

```bash
git clone https://github.com/AshPiBit02/python-chronicles.git
cd python-chronicles
```

### Run an example

Many scripts can be run directly from their own directory. For example:

```bash
python 01_basics/countdown.py
python 03_advanced/design_pattern/Behavioral/observer.py
```

Some project scripts import files from the same project directory, so run them from that directory. For example:

```bash
cd "04_projects/Design_patterns/Coffee Shop Billing System"
python main.py
```

## Learning goals

This repository is intended for practicing and revisiting:

- Python syntax and built-in data structures
- Functions, modules, exceptions, and file I/O
- Encapsulation, inheritance, composition, and polymorphism
- Common object-oriented design patterns
- Small, self-contained applications that combine these concepts

## License

This project is licensed under the [MIT License](LICENSE).
