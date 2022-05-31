def func1():
    with open('input21-2021.txt') as f:
        lines = f.read().splitlines()

    p1 = 4
    p2 = 6
    s1 = 0
    s2 = 0

    dice = 1
    turn = 1

    while True:
        if s1 >= 1000 or s2 >= 1000:
            # min(s1, s2) is the score below 1000, while dice - 1 is the number of total rolls
            print(min(s1, s2) * (dice - 1))
            break

        rolls = 0
        for i in range(3):
            rolls += (dice + i - 1) % 100 + 1

        if turn == 1:
            p1 = (p1 + rolls - 1) % 10 + 1
            s1 += p1
        else:
            p2 = (p2 + rolls - 1) % 10 + 1
            s2 += p2

        # Flip whose turn it is and increase the dice value
        turn = 3 - turn
        dice += 3


def func2():
    with open('input21-2021.txt') as f:
        lines = f.read().splitlines()

    mp = {}

    def recur(turn, p1, p2, s1, s2):
        key = str(turn) + ' ' + str(p1) + ' ' + str(p2) + ' ' + str(s1) + ' ' + str(s2)

        if key in mp:
            return mp[key]

        if s1 >= 21:
            return [1, 0]
        if s2 >= 21:
            return [0, 1]

        ans = [0, 0]

        if turn == 1:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        new_p1 = (p1 + i + j + k - 1) % 10 + 1
                        res = recur(2, new_p1, p2, s1 + new_p1, s2)
                        ans[0] += res[0]
                        ans[1] += res[1]

        else:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        new_p2 = (p2 + i + j + k - 1) % 10 + 1
                        res = recur(1, p1, new_p2, s1, s2 + new_p2)
                        ans[0] += res[0]
                        ans[1] += res[1]
        mp[key] = ans
        return ans

    print(max(recur(1, 4, 6, 0, 0)))


func1()
func2()
