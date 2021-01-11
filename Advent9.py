def findPrime():
    int_list = []
    f = open("input8.txt", "r")
    for line in f:
        int_list.append(int(line))

    preamble = int_list[:25]
    preamble.sort()

    possible_primes = int_list[25:]

    print(preamble, end="")
    print(possible_primes, end="")
    current_index = 25
    for possible_prime in possible_primes:

        valid = False

        for i in range(len(preamble)):

            for j in range(len(preamble)):

                if preamble[i] + preamble[j] == possible_prime:

                    print(preamble[i], preamble[j], possible_prime)
                    valid = True
                    break
            if valid:
                break
        if not valid:
            return possible_prime

        print(int_list[current_index])
        preamble.append(int_list[current_index])
        preamble.pop(0)
        current_index += 1

    return "No answer"


with open("input8.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in fp.readlines()]


# lines

def challenge1(codes, premable):
    previous_stack = []
    i = 0
    start = 0
    end = start + premable
    curr_index = premable
    while curr_index < len(codes) - 1:
        stack = codes[start:end]
        if curr_index > len(stack) - 1:
            start += 1
            end += 1
            valid = False
            for i in stack[:-1]:
                for j in stack[1:]:
                    # print(codes[curr_index], i, j)
                    if i + j == codes[curr_index]:
                        valid = True
                        break
                    else:
                        valid = False
                if valid:
                    break
            if not valid:
                return codes[curr_index]

        curr_index += 1

        print(stack)
        # break


# print(challenge1(lines, 25))

print(findPrime())
