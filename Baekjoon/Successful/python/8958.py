# c = int(input())
# for i in range(c):
#     score = input()
#     totalScore = 0
#     s = 1
#     for j in range(len(score)):
#         if score[j] == 'O':
#             totalScore += s
#             s += 1
#         else:
#             s = 1
#     print(totalScore)

case = int(input())
for i in range(case):
    answer = input()
    score = 1
    totalScore = 0
    for j in range(len(answer)) :
        if answer[j] == 'O':
            totalScore += score
            score += 1
        elif answer[j] == 'X' :
            score = 1
    print(totalScore)