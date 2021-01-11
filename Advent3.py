def advent3part1():
    f = open("input3.txt", "r")

    contents = f.readlines()

    tree_count = 0

    line_count = 0

    x = 0

    line_length = len(contents[0]) - 1  # 31
    # print(line_length)
    new = []
    for line in contents:
        # print(line[x], x)
        line_count += 1
        if line[x] == "#":
            tree_count += 1
            line = line[:x] + "X" + line[x:]
            # print(line[x], x, tree_count, line_count)
        else:
            line = line[:x] + "O" + line[x:]
        new.append(line)
        x = (x + 3) % line_length

    print(new)
    return tree_count


def advent3part2(right):
    f = open("input3.txt", "r")

    contents = f.readlines()

    tree_count = 0

    line_count = 0

    x = 0

    line_length = len(contents[0]) - 1  # 31
    print(line_length)
    for line in contents:
        # print(line[x], x)
        line_count += 1
        if line[x] == "#":
            tree_count += 1

            # print(line[x], x, tree_count, line_count)

            line = line[:x] + "O" + line[x:]

        x = (x + right) % line_length

    # print(contents)

    return tree_count


def advent3part2_down2(right):
    f = open("input3.txt", "r")

    contents = f.readlines()

    tree_count = 0

    line_count = 0

    x = 0

    line_length = len(contents[0]) - 1  # 31
    print(line_length)
    for line in contents:

        # print(line[x], x)

        if line_count % 2 == 0:
            if line[x] == "#":
                tree_count += 1

               # print(line[x], x, tree_count, line_count)

                line = line[:x] + "X" + line[x:]
            else:
                line = line[:x] + "O" + line[x:]
            x = (x + right) % line_length
        line_count += 1
        print(line)

    return tree_count


A = []

# A.append(advent3part1())

A.append(advent3part2(1))
A.append(advent3part2(3))
A.append(advent3part2(5))
A.append(advent3part2(7))
A.append(advent3part2_down2(1))

print(A)
