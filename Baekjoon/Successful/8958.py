c = int(input())
for i in range(c):
    score = input()
    totalScore = 0
    s = 1
    for j in range(len(score)):
        if score[j] == 'O':
            totalScore += s
            s += 1
        else:
            s = 1
    print(totalScore)