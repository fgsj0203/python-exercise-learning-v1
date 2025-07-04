import math

point_plane_x_y_one = input().split()
point_plane_x_y_two = input().split()
x1 = float(point_plane_x_y_one[0])
x2 = float(point_plane_x_y_two[0])
y1 = float(point_plane_x_y_one[1])
y2 = float(point_plane_x_y_two[1])

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("%.3f " % distance)
