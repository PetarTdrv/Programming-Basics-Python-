from math import pi

figure = input()

if figure == "square":
    side_a = float(input())
    area = side_a * side_a
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    area = pi * (radius * radius)
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input())
    height_to_side_a = float(input())
    area = side_a * height_to_side_a / 2
    print(f"{area:.3f}")
