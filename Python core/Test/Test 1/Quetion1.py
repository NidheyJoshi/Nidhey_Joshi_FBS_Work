
# Accept input from user
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))

# Rectangle calculations
rect_area = length * breadth
rect_perimeter = 2 * (length + breadth)

# Circle calculations
circle_area = 3.14159 * radius * radius
circle_circumference = 2 * 3.14159 * radius

# Display results
print("\n--- Rectangle ---")
print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")

print("\n--- Circle ---")
print(f"Area of circle: {circle_area}")
print(f"Circumference of circle: {circle_circumference}")
