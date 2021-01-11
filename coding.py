import sys


def tree():
    relations = {}
    split_lines = (line.split("/") for line in sys.stdin)
    for parent, child in split_lines:
        relations.setdefault(parent, []).append(child)
    return relations


def normalise_hierarchy(relations, parent='Vodafone'):
    try:
        children = relations[parent]
        for child in children:
            sub_hierarchy = normalise_hierarchy(relations, child)
            for element in sub_hierarchy:
                try:
                    yield (parent, *element)
                except TypeError:
                    yield (parent, child)
    except KeyError:
        yield None


print(normalise_hierarchy(tree()))
