def advent1part1():
    f = open("input-2021.txt", "r")

    contents = f.readlines()
    count = -1
    previous = 0
    for i in contents:
        if previous < int(i):
            count += 1
        previous = int(i)
    print(count)


def advent1part2():
    f = open("input-2021.txt", "r")
    contents = f.readlines()
    list = [0] * 3
    previous_total = 0
    total = 0
    index = 0
    count = 0

    for i in contents:
        if index > 2:
            index = 0

            total = sum_of_list(list)
            if previous_total < total:
                count += 1
            print(total, previous_total, list, count)
            previous_total = total
        else:
            list[index] = int(i)
            index += 1
    print(count, list)


def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total


# advent1part1()
advent1part2()
