valid = 0

input = open('input.txt', 'r')  # .split("\n")


def getPass(input):
    passPolicy, actualPass = input.readline().split(":")
    actualPass = actualPass.replace("\n", "")
    actualPass = actualPass.replace(" ", "")

    min, max = passPolicy.split("-")
    max, restrictedLetter = max.split(" ")
    password = [min, max, restrictedLetter, actualPass]
    return password


def oldPassPolicy(input):
    for i in range(1000):
        counter = 0
        password = getPass(input)
        for i in password[3]:
            if i == password[2]:
                counter += 1

        if counter >= int(password[0]) and counter <= int(password[1]):
            valid += 1


for i in range(1000):
    counter = 0
    password = getPass(input)
    # for i in range(len(password[3])):
    if password[3][int(password[0]) - 1] == password[2]:
        counter += 1
    if password[3][int(password[1]) - 1] == password[2]:
        counter += 1
    if counter == 1:
        valid += 1

print(valid)
