print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

PT = 3.1415
radius = float("input radius :")

area = PT * radius **2
circumference = 2 * PT * radius

print("radius is :",radius)
print("Area of this circle :",area)
print("circumference is :",circumference)