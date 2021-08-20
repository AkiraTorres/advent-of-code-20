input = open("input.txt", "r").read().split("\n")
input = [[i[0], i[1:]] for i in input]


def one(input):
    facing = ["E", 90]
    lon, lat = 0, 0

    for i in input:
        instruction = i[0]
        if instruction == "R":
            facing[1] += int(i[1])
            if facing[1] >= 360:
                facing[1] -= 360
            if facing[1] == 0:
                facing[0] = "N"
            if facing[1] == 90:
                facing[0] = "E"
            if facing[1] == 180:
                facing[0] = "S"
            if facing[1] == 270:
                facing[0] = "W"
        if instruction == "L":
            if int(i[1]) == 90:
                facing[1] += 270
            if int(i[1]) == 180:
                facing[1] += 180
            if int(i[1]) == 270:
                facing[1] += 90
            if facing[1] >= 360:
                facing[1] -= 360
            if facing[1] == 0:
                facing[0] = "N"
            if facing[1] == 90:
                facing[0] = "E"
            if facing[1] == 180:
                facing[0] = "S"
            if facing[1] == 270:
                facing[0] = "W"

        if instruction == "F":
            instruction = facing[0]

        if instruction == "N":
            lat += int(i[1])
        if instruction == "S":
            lat -= int(i[1])
        if instruction == "E":
            lon += int(i[1])
        if instruction == "W":
            lon -= int(i[1])

    return abs(lat) + abs(lon)


def two(input):
    wp = [10, 1]
    lon, lat = 0, 0

    for i in input:
        instruction = i[0]

        if instruction == "R":
            if int(i[1]) == 90:
                wp = [wp[1], wp[0] * -1]
            if int(i[1]) == 180:
                wp = [wp[0] * -1, wp[1] * -1]
            if int(i[1]) == 270:
                wp = [wp[1] * -1, wp[0]]

        if instruction == "L":
            if int(i[1]) == 90:
                wp = [wp[1] * -1, wp[0]]
            if int(i[1]) == 180:
                wp = [wp[0] * -1, wp[1] * -1]
            if int(i[1]) == 270:
                wp = [wp[1], wp[0] * -1]

        elif instruction == "F":
            lon += wp[0] * int(i[1])
            lat += wp[1] * int(i[1])

        if instruction == "N":
            wp[1] += int(i[1])
        elif instruction == "S":
            wp[1] -= int(i[1])
        elif instruction == "E":
            wp[0] += int(i[1])
        elif instruction == "W":
            wp[0] -= int(i[1])
    print(lon, lat)
    return abs(lat) + abs(lon)


# print(one(input))
print(two(input))
