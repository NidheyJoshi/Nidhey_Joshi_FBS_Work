import math

# Program to calculate area of an equilateral triangle

# Taking input from user
side = float(input("Enter the side of the equilateral triangle: "))

# Calculating area
area = (math.sqrt(3) / 4) * (side ** 2)

# Displaying result
print("\n--- Result ---")
print(f"Side: {side}")
print(f"Area of Equilateral Triangle: {area:.2f}")
