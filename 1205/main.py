
input = open('input.txt', 'r')


#actualPass = "FBFBBFFRLR"
#actualPass = ["FBFBBFFRLR", "BFBBFFFLRR", "FFBFBBBLLL", "FBFBFBFLLL"]


def getPass(input):
    higherPassId = 0
    passId = 0
    passesId = []
    for i in range(815):
        initialRow, finalRow = 0, 127
        initialColumn, finalColumn = 0, 7
        row = [initialRow, finalRow]
        column = [initialColumn, finalColumn]

        actualPass = input.readline()
        for j in actualPass:
            diferencaRow = finalRow - initialRow
            diferencaColumn = finalColumn - initialColumn
            if j == 'F':
                finalRow = diferencaRow // 2 + initialRow
                row[1] = finalRow
            elif j == 'B':
                initialRow = diferencaRow // 2 + initialRow + 1
                row[0] = initialRow
            elif j == 'L':
                if diferencaColumn != 1:
                    finalColumn = diferencaColumn // 2 + initialColumn
                    column[1] = finalColumn
                else:
                    if column[0] < column[1]:
                        column = column[0]
            elif j == 'R':
                if diferencaColumn != 1:
                    initialColumn = diferencaColumn // 2 + initialColumn + 1
                    column[0] = initialColumn
                else:
                    if column[0] > column[1]:
                        column = column[0]
                    else:
                        column = column[1]

        actualPassId = (row[0] * 8) + column
        passesId.append(actualPassId)
        passesId = sorted(passesId)

        if actualPassId > higherPassId:
            higherPassId = actualPassId

        for i in range(len(passesId) - 1):
            # print(passesId[i + 1])
            if passesId[i+1] == passesId[i] + 2:
                passId = passesId[i] + 1
    return passId


print(getPass(input))
