# Program to calculate third angle of a triangle

# Taking input from user
angle1 = float(input("Enter first angle of the triangle: "))
angle2 = float(input("Enter second angle of the triangle: "))

# Sum of angles in a triangle is always 180
angle3 = 180 - (angle1 + angle2)

# Displaying result
print("\n--- Result ---")
print(f"First Angle: {angle1}")
print(f"Second Angle: {angle2}")
print(f"Third Angle: {angle3}")
