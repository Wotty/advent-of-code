def findSanta():
    f = open("input2_2015.txt", "r")
    area = 0
    for line in f:
        l_s, w_s, h_s = line.split("x")
        l = int(l_s)
        w = int(w_s)
        h = int(h_s)
        area_1 = 2 * l * w
        area_2 = 2 * w * h
        area_3 = 2 * h * l
        area_4 = min(area_3,area_2,area_1)/2
        area += area_4 + area_3 + area_2 + area_1

    return area
def findSanta2():
    f = open("input2_2015.txt", "r")
    ribbon = 0
    for line in f:
        dimensions = [int(s) for s in line.split('x')]
        dimensions.sort()
        print(dimensions[0], dimensions[1], dimensions[2])
        ribbon += 2 * (dimensions[0] + dimensions[1])
        ribbon += dimensions[0]*dimensions[1]*dimensions[2]

    return ribbon

print(findSanta2())
