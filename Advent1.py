def advent1part1():
    f = open("input.txt", "r")

    contents = f.readlines()
    a = []
    count = 0
    for i in contents:

        a.append(int(i))

        for j in range(len(a) - 1):

            if (a[count] + a[j]) == 2020:
                return a[count] * a[j]

            # print(a[count], a[j])
        count += 1


def advent1part2():
    f = open("input.txt", "r")

    contents = f.readlines()
    a = []
    count = 0
    for i in contents:

        a.append(int(i))

        for j in range(len(a) - 1):

            for k in range(len(a) - 1):

                if (a[count] + a[j] + a[k]) == 2020:
                    print(a[count], a[j], a[k])
                    return a[count] * a[j] * a[k]

            # print(a[count], a[j])
        count += 1


# print(advent1part1())
print(advent1part2())
