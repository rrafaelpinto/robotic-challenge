### `Thoughtful Package Sorter`

### Project Overview

This repository contains a solution to the FDE Technical Screen challenge for Thoughtful's robotic automation factory. The goal is to implement a Python function that sorts packages into different stacks based on specific criteria related to their dimensions and mass.

-----

### The Challenge

The core task is to create a function that dispatches packages to one of three stacks: `STANDARD`, `SPECIAL`, or `REJECTED`. The sorting logic is based on whether a package is considered "bulky" or "heavy."

#### **Sorting Rules:**

A package is classified as **bulky** or **heavy** according to these rules:

  - **Bulky:**
      - Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
      - **OR** any single dimension (width, height, or length) is greater than or equal to 150 cm.
  - **Heavy:**
      - Its mass is greater than or equal to 20 kg.

#### **Dispatching Stacks:**

Based on the rules above, packages are dispatched to the following stacks:

  - **`REJECTED`**: If the package is **both** heavy and bulky.
  - **`SPECIAL`**: If the package is **either** heavy **or** bulky, but not both.
  - **`STANDARD`**: If the package is **neither** heavy **nor** bulky.

-----

### Implementation

The solution is implemented in Python. The main function is defined with the following signature:

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
```

### Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rrafaelpinto/robotic-challenge.git
    cd robotic-challenge
    ```

2.  **Run the code:**
    The `sort` function can be called directly from any Python script. Here is an example:

<!-- end list -->
```python
from sorter import sort

# Example 1: A standard package
print(f"Package (100x10x10, 5kg) is: {sort(100, 10, 10, 5)}")

# Example 2: A bulky package
print(f"Package (200x50x50, 15kg) is: {sort(200, 50, 50, 15)}")

# Example 3: A heavy package
print(f"Package (10x10x10, 25kg) is: {sort(10, 10, 10, 25)}")

# Example 4: A rejected package
print(f"Package (160x50x50, 30kg) is: {sort(160, 50, 50, 30)}")
```

### Author

  * [Rafael Pinto](https://www.linkedin.com/in/rafaelmpinto/)