import re


def find_santa():
    with open("input5_2015.txt", "r") as file:
        data = file.readlines();

        nice_count = 0
        for line in data:
            vowel_count = 0
            last_char = ''
            is_double_char = False

            for char in line:
                if char in "aeiou":
                    vowel_count += 1
                if char == last_char:
                    is_double_char = True
                last_char = char

            if vowel_count >= 3 and is_double_char and ("ab" not in line) and ("cd" not in line) and (
                    "pq" not in line) and ("xy" not in line):
                print(line)
                nice_count += 1
    return nice_count


def find_santa2():
    with open("input5_2015.txt", "r") as file:
        data = file.readlines()

        nice_count = 0
        for line in data:
            nice_dict = {}
            vowel_count = 0
            last_char = ''
            two_last_char = ''
            is_double_char = False

            for char in line:
                if char in "aeiou":
                    vowel_count += 1
                if char == last_char:
                    is_double_char = True

                two_last_char = last_char

                nice_dict[char + last_char] += 1
                last_char = char
            if vowel_count >= 3:
                print(line)
                nice_count += 1
    return nice_count


print(find_santa())
print(find_santa2())
