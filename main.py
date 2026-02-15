def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the correct stack for a package based on dimensions and mass.
    Returns: "STANDARD", "SPECIAL", or "REJECTED"
    """

    if any(value <= 0 for value in [width, height, length, mass]):
        raise ValueError("All inputs must be positive numbers.")

    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# Simple test cases
if __name__ == "__main__":
    print(sort(100, 100, 100, 10))   # STANDARD
    print(sort(200, 100, 100, 10))   # SPECIAL
    print(sort(100, 100, 100, 25))   # SPECIAL
    print(sort(200, 200, 200, 25))   # REJECTED
