def resetInput(input):
    for i in range(len(input)):
        input[i] = input[i].replace(".", "")
    return input


def boot(input):
    acc = 0
    counter = 0
    for i in input:
        try:
            instruction = input[counter].replace("\n", "").split(" ")
        except:
            return acc

        if instruction[0] == "nop":
            input[counter] = (
                instruction[0].replace("nop", ".nop") + " " + instruction[1]
            )
            counter += 1
        if instruction[0] == "acc":
            input[counter] = (
                instruction[0].replace("acc", ".acc") + " " + instruction[1]
            )
            acc += int(instruction[1])
            counter += 1
        if instruction[0] == "jmp":
            input[counter] = (
                instruction[0].replace("jmp", ".jmp") + " " + instruction[1]
            )
            if instruction[1][0] == "+":
                counter += int(instruction[1])
            else:
                counter += int(instruction[1])
            continue
        if (
            instruction[0] == ".nop"
            or instruction[0] == ".acc"
            or instruction[0] == ".jmp"
        ):
            input = resetInput(input)
            return 0
    return acc


def main():
    # input = open("inputTest.txt", "r").read().split("\n")
    input = open("input.txt", "r").read().split("\n")
    for k in range(8):
        for i in range(len(input)):
            instruction = input[i].replace("\n", "").split(" ")
            if instruction[0] == "nop":
                input[i] = "jmp " + instruction[1]
                result = boot(input)
                if result == 0:
                    input[i] = "nop " + instruction[1]
                    continue
                else:
                    return result
            elif instruction[0] == "jmp":
                input[i] = "nop " + instruction[1]
                result = boot(input)
                if result == 0:
                    input[i] = "jmp " + instruction[1]
                    continue
                else:
                    return result


if __name__ == "__main__":
    print(main())