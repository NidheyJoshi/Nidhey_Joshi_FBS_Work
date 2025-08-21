# Program to calculate Compound Interest

# Taking input from user
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time (in years): "))
R = float(input("Enter the Rate of Interest: "))

# Calculating Compound Interest
A = P * (1 + R/100) ** T   # Final Amount
CI = A - P                 # Compound Interest

# Displaying result
print("\n--- Result ---")
print(f"Principal (P): {P}")
print(f"Time (T): {T} years")
print(f"Rate (R): {R}%")
print(f"Compound Interest: {CI:.2f}")
print(f"Total Amount (Principal + CI): {A:.2f}")
