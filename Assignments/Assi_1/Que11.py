import math

# Program to calculate area and circumference of a circle

# Taking input from user
radius = float(input("Enter the radius of the circle: "))

# Calculations
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# Displaying results
print("\n--- Result ---")
print(f"Radius: {radius}")
print(f"Area of Circle: {area:.2f}")
print(f"Circumference of Circle: {circumference:.2f}")
