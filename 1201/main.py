input = open("input.txt", "r").read().split("\n")


def findTwoEntries(input):
    for i in input:
        for j in input:
            if int(i) + int(j) == 2020:
                print(f"{i} + {j} = 2020")
                return [int(i), int(j)]


def findTreeEntries(input):
    for i in input:
        for j in input:
            for k in input:
                if int(i) + int(j) + int(k) == 2020:
                    print(f"{i} + {j} + {k} = 2020")
                    return [int(i), int(j), int(k)]


def main(input):
    twoEntries = findTwoEntries(input)
    print(f"{twoEntries[0]} * {twoEntries[1]} = {twoEntries[0] * twoEntries[1]}")
    treeEntries = findTreeEntries(input)
    print(
        f"{treeEntries[0]} * {treeEntries[1]} * {treeEntries[2]} = {treeEntries[0] * treeEntries[1] * treeEntries[2]}"
    )


if __name__ == "__main__":
    main(input)