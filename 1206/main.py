
input = open('input.txt', 'r').read().split("\n\n")
answer1 = 0
answer2 = 0

#input = ["abc", "abc", "abc", "a", "b"]

for i in input:
    answers = []
    allAnswers = []
    countedAnswers = []
    counter = 0
    group = i.split("\n")
    personsInGroup = 0

    for j in group:
        personsInGroup += 1
        for k in j:
            allAnswers.append(k)
            if answers.count(k) == 0:
                answers.append(k)
                counter += 1
    answer1 += counter

    for i in allAnswers:
        if allAnswers.count(i) == personsInGroup and countedAnswers.count(i) == 0:
            countedAnswers.append(i)
            answer2 += 1


print(answer1)
print(answer2)
