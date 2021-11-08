import itertools


def findSanta():
    x_s = 0
    y_s = 0
    x_r = 0
    y_r = 0
    flipper = False
    coord_set = set()
    with open("input3_2015.txt", "r") as f:
        for c in itertools.chain.from_iterable(f):
            print(c)
            if not flipper:
                if c == "<":
                    x_r -= 1
                elif c == ">":
                    x_r += 1
                elif c == "^":
                    y_r += 1
                elif c == "v":
                    y_r -= 1
                flipper = not flipper
                coord_set.add(str(x_r) + ", " + str(y_r))
            elif flipper:
                if c == "<":
                    x_s -= 1
                elif c == ">":
                    x_s += 1
                elif c == "^":
                    y_s += 1
                elif c == "v":
                    y_s -= 1
                flipper = not flipper
                coord_set.add(str(x_s) + ", " + str(y_s))

            print(str(x_r) + ", " + str(y_r))

        return len(coord_set)


print(findSanta())
