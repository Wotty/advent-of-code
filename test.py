import sys

A = []
change = ""


register_list = {
        'PENNY': .01,
        'NICKEL': .05,
        'DIME': .10,
        'QUARTER': .25,
        'HALF DOLLAR': .50,
        'ONE': 1.00,
        'TWO': 2.00,
        'FIVE': 5.00,
        'TEN': 10.00,
        'TWENTY': 20.00,
        'FIFTY': 50.00,
        'ONE HUNDRED': 100.00
}

for line in sys.stdin:
    A = line.split(";")
    PP = float(A[0])
    CH = float(A[1])

    if CH < PP:
        print("ERROR")
    elif CH == PP:
        print("ZERO")
    else:
        CN = CH - PP  # Change needed
        print(CN)
        while CH > PP:
            print("A")
            for cash in register_list:

                if CH - cash > 0:

                    change = change + ", " + cash

print(change)