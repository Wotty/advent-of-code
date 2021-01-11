import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))


def shortestDistance(points, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(points[i], points[j]) < min_val:
                min_val = dist(points[i], points[j])

    return min_val


first_line = 1
P = []
for line in sys.stdin:
    if first_line:
        n = line
        first_line = 0
    if " " in line:

        if line == "0":
            pass
        else:
            # print(line)
            point_list = line.split(" ")
            x = float(point_list[0])
            y = float(point_list[1])
            P.append(Point(x, y))

print(shortestDistance(P, n))
