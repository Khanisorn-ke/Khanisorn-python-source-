def calculate_rectangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * base
    print(f"Rectangle with base {base} and width {height}")
    print(f"Area = {base} × {height} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

