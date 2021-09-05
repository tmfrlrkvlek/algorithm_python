case = int(input())
count = [0] * 26

for i in range(case):
    name = input()
    count[ord(name[0])-97] += 1

player = 0
for i in range(26):
    if count[i] >= 5:
        print(chr(i + 97), end="")
        player+=1

if player==0:
    print("PREDAJA")