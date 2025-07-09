side_triangle_one = int(input("side one: "))
side_triangle_two = int(input("side two: "))
side_triangle_three = int(input("side three: "))

if (side_triangle_one + side_triangle_two) > side_triangle_three:
    if (
        side_triangle_one == side_triangle_two
        and side_triangle_two == side_triangle_three
        and side_triangle_one == side_triangle_three
    ):
        print("Triangle equilater")
    elif (
        (side_triangle_one == side_triangle_two)
        or (side_triangle_two == side_triangle_three)
        or (side_triangle_one == side_triangle_three)
    ):
        print("Triangle isosceles")
    elif (
        (side_triangle_one != side_triangle_two)
        or (side_triangle_one != side_triangle_three)
        or (side_triangle_two != side_triangle_three)
    ):
        print("Triangle Scalene ")
else:
    print("Triangle invalid")
