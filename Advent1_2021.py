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


advent1part1()
