from models import Package


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

    for name, value in zip(["width", "height", "length", "mass"], [width, height, length, mass]):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number (int or float), received: {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero. Received: {value}")

    package = Package(width, height, length, mass)
    return package.get_stack()
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sort a package into a stack based on its dimensions and mass.")
    parser.add_argument("width", type=float, help="Width of the package in centimeters.")
    parser.add_argument("height", type=float, help="Height of the package in centimeters.")
    parser.add_argument("length", type=float, help="Length of the package in centimeters.")
    parser.add_argument("mass", type=float, help="Mass of the package in kilograms.")

    args = parser.parse_args()

    result = sort(args.width, args.height, args.length, args.mass)
    print(result)