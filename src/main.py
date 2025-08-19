

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
    BULKY_VOLUME = 1000000
    BULKY_DIMENSION = 150
    HEAVY_MASS = 20
    
    is_bulky = False
    if (width * height * length) >= BULKY_VOLUME:
        is_bulky = True
    elif width >= BULKY_DIMENSION or height >= BULKY_DIMENSION or length >= BULKY_DIMENSION:
        is_bulky = True

    is_heavy = False
    if mass >= HEAVY_MASS:
        is_heavy = True

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    sort(10, 20, 30, 5)