import math

# Function to calculate circumference
def circumference(radius):
    """
    Calculate the circumference of a circle.
    Formula: C = 2 * π * r
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius

# Main program
try:
    r = float(input("Enter the radius of the circle: "))
    c = circumference(r)
    print(f"The circumference of the circle is: {c:.2f}")
except ValueError as e:
    print(f"Error: {e}")
