
# Input: wall area
area_one_wall = float(input("Enter area of one wall (sq.ft): "))

# Input: cost rates
cost_interior = float(input("Enter cost of painting per sq.ft for interior: "))
cost_exterior = float(input("Enter cost of painting per sq.ft for exterior: "))

# Number of walls
interior_walls = 7   # all 7 walls painted inside
exterior_walls = 6   # outside walls only

# Total areas
total_interior_area = interior_walls * area_one_wall
total_exterior_area = exterior_walls * area_one_wall

# Total cost
total_interior_cost = total_interior_area * cost_interior
total_exterior_cost = total_exterior_area * cost_exterior

# Print result
print("\n--- Painting Cost Calculation ---")
print(f"Total interior wall area: {total_interior_area} sq.ft")
print(f"Total exterior wall area: {total_exterior_area} sq.ft")
print(f"Interior painting cost: ₹{total_interior_cost}")
print(f"Exterior painting cost: ₹{total_exterior_cost}")
print(f"Grand Total: ₹{total_interior_cost + total_exterior_cost}")
