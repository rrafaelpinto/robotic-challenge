

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
    print(f"Sorting package with dimensions ({width} cm, {height} cm, {length} cm) and mass {mass} kg")

if __name__ == "__main__":
    sort(10, 20, 30, 5)