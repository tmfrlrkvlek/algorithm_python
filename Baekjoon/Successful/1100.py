# total = 0
# for i in range(8):
#     line = input()
#     for j in range(8):
#         if (i + j) % 2 == 0 and line[j] == 'F':
#                 total += 1
# print(total)

# ----------------찬희님 코드 ---------
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
h=input()

white_first=list(a+c+e+g)
black_first=list(b+d+f+h)

answer=0

for i in range(0,32):
    if i%2==0:
        if white_first[i]=='F':
            answer=answer+1

for i in range(0,32):
    if i%2==1:
        if black_first[i]=='F':
            answer=answer+1

print(answer)