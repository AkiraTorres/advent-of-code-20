input = open("input.txt", "r").read().split("\n")


def adjustInput(input):
    newInput = [[input[i][j] for j in range(len(input[0]))] for i in range(len(input))]
    return newInput


input = adjustInput(input)


def getCell(matrix, x, y):
    value = 0
    if y >= 0 and x >= 0 and x < len(matrix) and y < len(matrix[0]):
        value = matrix[x][y]
    else:
        value = "."
    return value


def getOccupiedSeatsOne(matrix, x, y):
    adjacent = [
        getCell(matrix, x - 1, y),
        getCell(matrix, x - 1, y + 1),
        getCell(matrix, x, y + 1),
        getCell(matrix, x + 1, y + 1),
        getCell(matrix, x + 1, y),
        getCell(matrix, x + 1, y - 1),
        getCell(matrix, x, y - 1),
        getCell(matrix, x - 1, y - 1),
    ]
    return adjacent.count("#")


def getTwoCell(matrix, x, y, flag):
    value = 0
    if y >= 0 and x >= 0 and x < len(matrix) and y < len(matrix[0]):
        if matrix[x][y] != ".":
            value = matrix[x][y]
        else:
            if flag == "up":
                value = getTwoCell(matrix, x - 1, y, "up")
            elif flag == "upRight":
                value = getTwoCell(matrix, x - 1, y + 1, "upRight")
            elif flag == "right":
                value = getTwoCell(matrix, x, y + 1, "right")
            elif flag == "downRight":
                value = getTwoCell(matrix, x + 1, y + 1, "downRight")
            elif flag == "down":
                value = getTwoCell(matrix, x + 1, y, "down")
            elif flag == "downLeft":
                value = getTwoCell(matrix, x + 1, y - 1, "downLeft")
            elif flag == "left":
                value = getTwoCell(matrix, x, y - 1, "left")
            elif flag == "upLeft":
                value = getTwoCell(matrix, x - 1, y - 1, "upLeft")
    else:
        value = "."
    return value


def getOccupiedSeatsTwo(matrix, x, y):
    adjacent = [
        getTwoCell(matrix, x - 1, y, "up"),
        getTwoCell(matrix, x - 1, y + 1, "upRight"),
        getTwoCell(matrix, x, y + 1, "right"),
        getTwoCell(matrix, x + 1, y + 1, "downRight"),
        getTwoCell(matrix, x + 1, y, "down"),
        getTwoCell(matrix, x + 1, y - 1, "downLeft"),
        getTwoCell(matrix, x, y - 1, "left"),
        getTwoCell(matrix, x - 1, y - 1, "upLeft"),
    ]
    return adjacent.count("#")


def partOne(input):
    newInput = [[input[i][j] for j in range(len(input[0]))] for i in range(len(input))]
    for row in range(len(input)):
        for column in range(len(input[0])):
            occupied = getOccupiedSeatsOne(input, row, column)
            if input[row][column] == ".":
                newInput[row][column] = "."
            elif occupied == 0:
                newInput[row][column] = "#"
            elif occupied >= 4:
                newInput[row][column] = "L"

    if newInput != input:
        partOne(newInput)
    else:
        occupied = 0
        for i in newInput:
            occupied += i.count("#")
        print(occupied)
        return occupied


def partTwo(input):
    newInput = [[input[i][j] for j in range(len(input[0]))] for i in range(len(input))]
    for row in range(len(input)):
        for column in range(len(input[0])):
            occupied = getOccupiedSeatsTwo(input, row, column)
            if input[row][column] == ".":
                newInput[row][column] = "."
            elif occupied == 0:
                newInput[row][column] = "#"
            elif occupied >= 5:
                newInput[row][column] = "L"

    if newInput != input:
        partTwo(newInput)
    else:
        occupied = 0
        for i in newInput:
            occupied += i.count("#")
        print(occupied)
        return occupied


partOne(input)
partTwo(input)
