"""
I got real stuck in the part 2, so I got this comment to understand better 
https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9mvrh?utm_source=share&utm_medium=web2x&context=3
after this I organized and improved my code of the part 1 using his solution too.
"""

input = open("input.txt", "r").read().split("\n")
adaptorsInput = [0] + sorted([int(i) for i in input])


def partOne():
    diffs = [
        adaptorsInput[i + 1] - adaptorsInput[i] for i in range(len(adaptorsInput) - 1)
    ]
    adaptorsInput.append(adaptorsInput[-1] + 3)
    diffs.append(3)

    return f"Part 1: {diffs.count(1) * diffs.count(3)}"


def partTwo():
    routes = {}
    routes[0] = 1

    for j in adaptorsInput[1:]:
        routes[j] = routes.get(j - 1, 0) + routes.get(j - 2, 0) + routes.get(j - 3, 0)

    return f"Part 2: {routes[max(routes.keys())]}"


def main():
    print(partOne())
    print(partTwo())


if __name__ == "__main__":
    main()