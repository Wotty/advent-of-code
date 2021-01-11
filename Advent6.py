def customs_questions():
    f = open("input6.txt", "r")
    group_set = set()
    group_questions = []
    previous_person = set()

    for line in f:
        person_set = set()

        if line == "\n":
            group_questions.append(len(group_set))
            print(len(group_set))
            group_set = set()
            person_set = set()
        else:
            for char in line.strip():
                person_set.add(char)

            if group_set == set():
                group_set = person_set
            else:
                group_set &= person_set  # cool equivalent of group_set &= person_set & group_set

            print(person_set, previous_person, group_set, len(group_set))
            previous_person = person_set

    return group_questions


def customs_questions_attempt_2():
    f = open("input6.txt", "r")
    group_set = set()
    group_questions = []
    previous_person = set()
    # Problem 6 - Custom customs
    with open('input6.txt', 'r') as f:
        groups = f.read().split("\n\n")

        for group in groups:
            group_members = group.split("\n")
            group_set = set(group_members[0])

            for group_member in group_members:
                print(group_set, group_member)
                group_set &= set(group_member)  # cool equivalent of group_set &= person_set & group_set

            group_questions.append(len(group_set))
    return group_questions


#    group_questions = customs_questions()
#  print(len(group_questions))
# print(group_questions)
# print(sum(group_questions))

group_questions = customs_questions_attempt_2()

print(len(group_questions))
print(group_questions)
print(sum(group_questions))
