c = int(input())
str = input()
for i in range(c - 1):
    str2 = input()
    for j in range(len(str2)):
        if str2[j] != str[j]:
            str = str[:j] + '?' + str[j+1:]

print(str)



    # print(' '.join(list(map(str, answer))))