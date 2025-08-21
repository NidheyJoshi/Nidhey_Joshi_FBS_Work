import cmath  # cmath handles complex numbers too

# Program to find roots of quadratic equation

# Taking input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculating discriminant
D = (b ** 2) - (4 * a * c)

# Finding roots using quadratic formula
root1 = (-b + cmath.sqrt(D)) / (2 * a)
root2 = (-b - cmath.sqrt(D)) / (2 * a)

# Displaying result
print("\n--- Result ---")
print(f"Discriminant (D): {D}")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
