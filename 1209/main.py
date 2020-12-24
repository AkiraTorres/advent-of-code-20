# input = open("inputTest.txt", "r").read().split("\n")
input = open("input.txt", "r").read().split("\n")


def findInvalidNumber():
    initalN = 25
    n = initalN
    for i in range(n, len(input)):
        for j in range(n - initalN, n):
            for k in range(n - initalN, n):
                if int(input[i]) == int(input[k]) + int(input[j]):
                    break
            if int(input[i]) == int(input[k]) + int(input[j]):
                break
        else:
            return input[i]
        n += 1


def getSumOfInvalidNumber(invalidNumber):
    n = 0
    while True:
        total = 0
        sumNumbers = []
        for i in range(n, len(input)):
            if int(input[i]) != int(invalidNumber):
                total += int(input[i])
                sumNumbers.append(int(input[i]))
            if total == int(invalidNumber):
                sumNumbers = sorted(sumNumbers)
                return sumNumbers[0] + sumNumbers[-1]
        n += 1


def main():
    invalidNumber = findInvalidNumber()
    print(invalidNumber)
    print(getSumOfInvalidNumber(invalidNumber))


if __name__ == "__main__":
    main()