# Program to calculate Simple Interest

# Taking input from user
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time (in years): "))
R = float(input("Enter the Rate of Interest: "))

# Calculating Simple Interest
SI = (P * T * R) / 100

# Displaying result
print("\n--- Result ---")
print(f"Principal (P): {P}")
print(f"Time (T): {T} years")
print(f"Rate (R): {R}%")
print(f"Simple Interest: {SI}")
