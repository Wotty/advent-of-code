def advent2part1():
    f = open("input2.txt", "r")

    contents = f.readlines()

    count = 0
    for line in contents:
        p_array = line.split(":")
        password = p_array[1]
        find_array = p_array[0].split(" ")
        char = find_array[1]
        range_array = find_array[0].split("-")
        min = int(range_array[0])
        max = int(range_array[1])
        numOfLetters = password.count(char)

        if min <= numOfLetters <= max:
            count += 1
        # print(numOfLetters)

    return count


def advent2part2():
    f = open("input2.txt", "r")

    contents = f.readlines()

    count = 0
    for line in contents:
        p_array = line.split(":")
        password = p_array[1]
        find_array = p_array[0].split(" ")
        char = find_array[1]
        range_array = find_array[0].split("-")
        min = int(range_array[0])
        max = int(range_array[1])
        numOfLetters = password.count(char)

        if (password[min] == char) ^ (password[max] == char):
            count += 1
            print(password)
        # print(numOfLetters)

    return count


# print(advent2part1())
print(advent2part2())
