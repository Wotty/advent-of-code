def Game():
    # Read File
    f = open("input9.txt", "r")
    contents = f.readlines()
    line_count = len(contents)
    current_line = 0
    executed_lines = set()

    # Accumulator
    accumulator = 0

    while line_count > current_line:

        operation, line = contents[current_line].split(" ")
        print(operation, line, current_line)
        if current_line not in executed_lines:
            executed_lines.add(current_line)

            if operation == "jmp":
                current_line += int(line)
            elif operation == "acc":
                accumulator += int(line)

        else:
            return accumulator

    return None


print(Game())