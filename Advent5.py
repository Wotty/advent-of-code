def advent5():
    f = open("input5.txt", "r")

    contents = f.readlines()

    max_id = 0

    w, h = 8, 128
    flight = [[0 for x in range(w)] for y in range(h)]

    for line in contents:
        row = line[:7]
        row = row.replace("B", "1")
        row = row.replace("F", "0")
        column = line[7:]
        column = column.replace("L", "0")
        column = column.replace("R", "1")

        row_num = int(row, 2)
        column_num = int(column, 2)

        flight[row_num][column_num] = 1

        id = row_num * 8 + column_num
        if id > max_id: max_id = id
        print(row, row_num, line)
        print(row_num, column_num, id)
    print(flight)

    row_count = 0
    for seat in flight:
        if 115 > row_count > 9:
            if 0 in seat:
                column_count = 2
                id = row_count * 8 + column_count
                print(seat, row_count, column_count, id)

        row_count += 1
    return max_id


print(advent5())
