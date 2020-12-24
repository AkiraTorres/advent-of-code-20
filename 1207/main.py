import re

input = open("input.txt", "r")
# input = open("inputTest.txt", "r")
rules = input.read().split("\n")

bags = ["shiny gold"]
answer1 = 0
answer2 = 0

for l in bags:
    for i in rules:
        if i == "":
            break
        mainBag, x = i.split(" bags contain ")
        x = x.split(", ")
        for j in range(len(x)):
            if re.match(r"(\d+) " + l + r" bag?[.]?", x[j]):
                if bags.count(mainBag) == 0:
                    answer1 += 1
                    bags.append(mainBag)
                break

bags = ["shiny gold"]
for l in bags:
    for i in rules:
        if i == "":
            break
        mainBag, x = i.split(" bags contain ")
        x = x.split(", ")
        if mainBag == l:
            for j in x:
                if j == "no other bags.":
                    break
                bag = j.replace(j[0], "")
                bag = bag.replace(".", "")
                bag = bag.replace("bags", "")
                bag = bag.replace("bag", "")
                bag = bag.strip()
                for m in range(int(j[0])):
                    bags.append(bag)
                answer2 += int(j[0])


print(answer1)
print(answer2)
# print(bags)