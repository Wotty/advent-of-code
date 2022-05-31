from collections import defaultdict


def parse(data):
    scanners = []
    for scanner in data:
        beacons = []
        for line in scanner.split("\n"):
            if "--" not in line:
                beacons.append(tuple([int(c) for c in line.split(",")]))
        scanners.append(beacons)
    return scanners


def rotate_point(p, rot):
    x, y, z = p
    if rot == 0:
        return x, y, z
    if rot == 1:
        return x, -z, y
    if rot == 2:
        return x, -y, -z
    if rot == 3:
        return x, z, -y
    if rot == 4:
        return -x, -y, z
    if rot == 5:
        return -x, -z, -y
    if rot == 6:
        return -x, y, -z
    if rot == 7:
        return -x, z, y
    if rot == 8:
        return y, x, -z
    if rot == 9:
        return y, -x, z
    if rot == 10:
        return y, z, x
    if rot == 11:
        return y, -z, -x
    if rot == 12:
        return -y, x, z
    if rot == 13:
        return -y, -x, -z
    if rot == 14:
        return -y, -z, x
    if rot == 15:
        return -y, z, -x
    if rot == 16:
        return z, x, y
    if rot == 17:
        return z, -x, -y
    if rot == 18:
        return z, -y, x
    if rot == 19:
        return z, y, -x
    if rot == 20:
        return -z, x, -y
    if rot == 21:
        return -z, -x, y
    if rot == 22:
        return -z, y, x
    if rot == 23:
        return -z, -y, -x


def add_points(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return x1 + x2, y1 + y2, z1 + z2


def sub_points(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return x1 - x2, y1 - y2, z1 - z2


def invert_point(p):
    x, y, z = p
    return -x, -y, -z


def manhattan_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


data = open("input19-2021.txt").read().strip().split("\n\n")
scanners = parse(data)
ocean = set(scanners.pop(0))
scanner_coords = [(0, 0, 0)]

while scanners:
    test_scanner = scanners.pop(0)
    match = False
    for rotation in range(24):
        offsets = defaultdict(int)
        for beacon in ocean:
            rotated_points = set()
            for point in test_scanner:
                rotated_point = rotate_point(point, rotation)
                x1, y1, z1 = beacon
                x2, y2, z2 = rotated_point
                offset = sub_points(rotated_point, beacon)
                offsets[offset] += 1
        for offset, ct in offsets.items():
            if ct >= 12:
                match = True
                scanner = invert_point(offset)
                scanner_coords.append(scanner)
                for point in test_scanner:
                    point = rotate_point(point, rotation)
                    ocean.add(add_points(point, scanner))
        continue
    if not match:
        scanners.append(test_scanner)
print(f"Part 1: {len(ocean)}")

scanner_distances = set()
while scanner_coords:
    p1 = scanner_coords.pop()
    for p2 in scanner_coords:
        scanner_distances.add(manhattan_distance(p1, p2))
print(f"Part 2: {max(scanner_distances)}")

