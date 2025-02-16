#1 Write a Python program to convert degree to radian.
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)  # Convert degrees to radians

# Get user input
degree = float(input("Input degree: "))

# Convert and print the result
radian = degree_to_radian(degree)
print(f"Output radian: {radian:.6f}")  # Format to 6 decimal places



#2 Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(height, base1, base2):
    return (height * (base1 + base2)) / 2  # Formula for the area of a trapezoid

# Given values
height = 5
base1 = 5
base2 = 6

# Calculate and print the area
area = trapezoid_area(height, base1, base2)
print(f"Expected Output: {area}")



#3 Write a Python program to calculate the area of regular polygon.
import math

def regular_polygon_area(sides, length):
    # Formula for the area of a regular polygon: (n * s^2) / (4 * tan(pi / n))
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

# Get user input for the number of sides and the length of each side
sides = int(input("Enter the number of sides of the polygon: "))
length = float(input("Enter the length of each side: "))

# Calculate and print the area
area = regular_polygon_area(sides, length)
print(f"The area of the regular polygon is: {area:.2f}")



#4 Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(base, height):
    return base * height  # Formula for the area of a parallelogram

# Get user input for base and height
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

# Calculate and print the area
area = parallelogram_area(base, height)
print(f"The area of the parallelogram is: {area}")
