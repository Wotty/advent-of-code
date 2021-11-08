def findSanta():
    result = open("input_2015.txt").read()
    count = 0

    for char in result:
        print(char)
        if char == "(":
            count += 1
        elif char == ")":
            count -=1

    return count
def findSanta2():
    result = open("input_2015.txt").read()
    count_floor = 0
    count_char = 1
    for char in result:
        if char == "(":
            count_floor += 1
        elif char == ")":
            count_floor -=1
        print(char, count_char, count_floor)
        if count_floor == -1:
            print(char, count_char,count_floor)
            return count_char
        count_char+=1

    return -1
# print(findSanta())
print(findSanta2())