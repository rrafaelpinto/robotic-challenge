
# Thoughtful Package Sorter

## Project Overview

This repository contains a Python solution for Thoughtful's robotic automation factory challenge. The goal is to implement a function that sorts packages into different stacks based on their dimensions and mass.

---

## Challenge Description

The main task is to create a function that dispatches packages to one of three stacks: `STANDARD`, `SPECIAL`, or `REJECTED`, according to whether a package is considered "bulky" or "heavy".

### Sorting Rules

A package is classified as **bulky** or **heavy** according to these rules:

- **Bulky:**
    - Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
    - **OR** any single dimension (width, height, or length) is greater than or equal to 150 cm.
- **Heavy:**
    - Its mass is greater than or equal to 20 kg.

### Dispatching Stacks

- `REJECTED`: If the package is **both** heavy and bulky.
- `SPECIAL`: If the package is **either** heavy **or** bulky, but not both.
- `STANDARD`: If the package is **neither** heavy **nor** bulky.

---

## Implementation

The main function is implemented in `src/main.py`:

```python
def sort(width, height, length, mass):
        """
        Sorts a package into a stack based on its dimensions and mass.

        Args:
                width (float): The width of the package in centimeters.
                height (float): The height of the package in centimeters.
                length (float): The length of the package in centimeters.
                mass (float): The mass of the package in kilograms.

        Returns:
                str: The name of the stack ("STANDARD", "SPECIAL", or "REJECTED").
        """
        # ...implementation...
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rrafaelpinto/robotic-challenge.git
cd robotic-challenge
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the code

You can call the `sort` function directly from your Python code:

```python
from src.main import sort

print(sort(100, 10, 10, 5))      # STANDARD
print(sort(200, 50, 50, 15))     # SPECIAL
print(sort(10, 10, 10, 25))      # SPECIAL
print(sort(160, 50, 50, 30))     # REJECTED
```

---

## Running Automated Tests

Automated tests are provided in the `tests` directory using `pytest`.

To run all tests:

```bash
pytest
```

If you encounter import errors, run:

```bash
PYTHONPATH=. pytest
```

---

## Project Structure

```
robotic-challenge/
├── src/
│   ├── main.py
│   └── __init__.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

---

## Author

[Rafael Pinto](https://www.linkedin.com/in/rafaelmpinto/)