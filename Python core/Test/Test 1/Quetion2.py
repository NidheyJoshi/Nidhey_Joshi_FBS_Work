# Simple Interest Calculation

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))

si = (p * r * t) / 100

print("Simple Interest =", si)
