input = open('input.txt', 'r').read().split("\n\n")


def valuesValidation(key, value):
    if key == "byr":
        if int(value) >= 1920 and int(value) <= 2002:
            return True
        else:
            return False

    if key == "iyr":
        if int(value) >= 2010 and int(value) <= 2020:
            return True
        else:
            return False

    if key == "eyr":
        if int(value) >= 2020 and int(value) <= 2030:
            return True
        else:
            return False

    if key == "hgt":
        height = ""
        if value[-1] == 'm':
            for i in range(3):
                height += value[i]
            if int(height) >= 150 and int(height) <= 193:
                return True
            else:
                return False
        elif value[-1] == 'n':
            for i in range(2):
                height += value[i]
            if int(height) >= 59 and int(height) <= 76:
                return True
            else:
                return False

    if key == "hcl":
        if value[0] == '#':
            for i in range(1, 7):
                if value[i].isalnum() == False:
                    return False
            return True
        else:
            return False

    if key == "ecl":
        if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
            return True
        else:
            return False

    if key == "pid":
        if value.isdigit() == True:
            if len(value) == 9:
                return True
            else:
                return False
        else:
            return False


def isValid(input):
    valid = 0
    for i in input:
        counter = 0
        validCounter = 0

        i = i.replace("\n", " ")
        i = i.replace(":", " ")
        actualPassport = i.split(" ")
        for j in actualPassport:
            counter += 1
            if j == 'byr' or j == 'iyr' or j == "eyr" or j == 'hgt' or j == 'hcl' or j == 'ecl' or j == 'pid':
                try:
                    if valuesValidation(j, actualPassport[counter]):
                        validCounter += 1
                except:
                    valid = valid
        # print(validCounter)
        if validCounter == 7:
            valid += 1

    return valid


validPassports = isValid(input)
print(validPassports)
