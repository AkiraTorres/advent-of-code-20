trees = 0


def treesQuantity(x, y):
    input = open('input.txt', 'r')
    actualLine = input.readline()
    initalPositionX, trees = 0, 0
    for i in range(322):
        for j in range(y):
            actualLine = input.readline()
        initalPositionX += x
        if initalPositionX >= 31:
            initalPositionX -= 31
        try:
            if actualLine[initalPositionX] == '#':
                trees += 1
        except:
            return trees

    input.close()
    return trees


def treesMultiplied():
    trees = 1
    for i in range(8):
        if i % 2 != 0:
            trees *= treesQuantity(i, 1)
    trees *= treesQuantity(1, 2)

    return trees


trees = treesMultiplied()
#trees = treesQuantity(input, 3, 1)
print(trees)
