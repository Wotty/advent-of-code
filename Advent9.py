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


print(findPrime())
