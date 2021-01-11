import re
from collections import defaultdict


def customs_questions():
    f = open("input7.txt", "r")
    bags = defaultdict(list)

    with open('input7.txt', 'r') as f:
        rules = f.read().split(".\n")

    for rule in rules:
        a = re.sub(r' bags| bag', '', rule)
        outer_bag, curr_inner_bags = a.split(" contain ")

        if curr_inner_bags != "no other ":

            for inner_bag in curr_inner_bags.split(', '):

                if outer_bag not in bags:
                    bags.update({outer_bag: [inner_bag]})
                else:
                    bags[outer_bag].append(inner_bag)

        else:
            print(outer_bag, "No inner bags")

    print(bags.keys())
    return bags


def count_trees(bags):
    count = 0
    for outer_bag, inner_bags in bags:
        for bag_count_str, inner_bag in inner_bags.split(" ", 1):
            bag_count = int(bag_count_str)

            count += count_trees()

    return count


bags = customs_questions()
# count_trees(bags)
print(bags.items())
