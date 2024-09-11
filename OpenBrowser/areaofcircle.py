def calculate_circle_area(radius):
    pi = 3.14

    area = pi * (radius ** 2)
    print(area)

    return area


radius = float(input("value of radius : "))
area = calculate_circle_area(radius)
print(f"final value of area of circle {area}")
