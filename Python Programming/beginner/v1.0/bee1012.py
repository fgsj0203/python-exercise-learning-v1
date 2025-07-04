all_sides = input().split()
side_a = float(all_sides[0])
side_b = float(all_sides[1])
side_c = float(all_sides[2])

triangle = side_a * side_c / (2)
circle = (3.14159) * (side_c**2)
trapezium = (side_a + side_b) * side_c / (2.0)
square = side_b * side_b
rectangle = side_a * side_b

# section of print values
print("Triangle: %.3f" % triangle)
print("Circle: %.3f" % circle)
print("Trapezium: %.3f" % trapezium)
print("Square: %.3f" % square)
print("Rectangle: %.3f" % rectangle)
