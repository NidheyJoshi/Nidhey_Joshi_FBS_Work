# Program to convert days into years, weeks and days

# Taking input from user
days = int(input("Enter number of days: "))

# Calculating years, weeks, and days
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7

# Displaying result
print("\n--- Result ---")
print(f"Total Days: {days}")
print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {days_left}")
