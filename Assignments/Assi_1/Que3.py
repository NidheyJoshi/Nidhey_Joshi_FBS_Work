# Program to find quotient and remainder

# Taking input from user
num1 = int(input("Enter the dividend (number to be divided): "))
num2 = int(input("Enter the divisor (number to divide by): "))

# Calculating quotient and remainder
quotient = num1 // num2   # Integer division
remainder = num1 % num2   # Modulus operator

# Displaying results
print("\n--- Result ---")
print(f"Dividend: {num1}")
print(f"Divisor: {num2}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
