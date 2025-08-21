import math

# Program to calculate volume of a sphere

# Taking input from user
radius = float(input("Enter the radius of the sphere: "))

# Calculating volume
volume = (4/3) * math.pi * (radius ** 3)

# Displaying result
print("\n--- Result ---")
print(f"Radius: {radius}")
print(f"Volume of Sphere: {volume:.2f}")
