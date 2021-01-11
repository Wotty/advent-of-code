import re


def read_all_passports():
    f = open("input4.txt", "r")

    passport_list = []  # list of passports
    keys = []
    values = []

    for line in f:

        if line == "\n":

            print(len(passport_list))
            print('keys', keys, 'values', values)

            if (len(keys) == 8 and len(values) == 8 and 'cid' in keys) or (
                    len(keys) == 7 and len(values) == 7 and 'cid' not in keys):
                passport = dict(zip(keys, values))
                passport_list.append(passport)

            # Clear keys and values
            keys = []
            values = []

        else:
            line = line.strip("\n")

            for field in line.split(" "):
                (key, value) = field.split(":")
                keys.append(key)
                values.append(value)

    return passport_list


def is_valid_passport(passport_list):
    passport_list_valid = []
    for passport in passport_list:
        valid = 0
        if 1920 <= int(passport.get('byr')) <= 2002:
            valid += 1
        print(valid, end=", ")
        if 2010 <= int(passport.get('iyr')) <= 2020:
            valid += 1
        print(valid, end=", ")
        if 2020 <= int(passport.get('eyr')) <= 2030:
            valid += 1
        print(valid, end=", ")
        try:
            unit = passport.get('hgt')[-2:]
            hgt_value = float(passport.get('hgt')[:-2])

            if unit == 'cm' and 150 <= hgt_value <= 193:
                valid += 1
            elif unit == 'in' and 59 <= hgt_value <= 76:
                valid += 1
        except ValueError:
            print(passport.get('hgt'), 'is not valid')
        print(valid, end=", ")
        if re.search('^#(\d|[a-f]){6}$', passport.get('hcl')):
            valid += 1
        print(valid, end=", ")
        if passport.get('ecl') in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            valid += 1
        print(valid, end=", ")
        if re.search('^\d{9}$', passport.get('pid')):
            valid += 1
        print(valid)
        if valid >= 7:
            passport_list_valid.append(passport)

    return passport_list_valid


passport_list = read_all_passports()

print(len(passport_list))

passport_list_valid = is_valid_passport(passport_list)

print('valid passports', len(passport_list_valid))
