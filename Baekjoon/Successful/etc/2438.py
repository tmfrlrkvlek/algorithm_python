n = int(input())

# for j in range(x):  
#     print('*',end='') 
#     for i in range(j):
#         print('*', end='')
#     print()

for i in range(1,n+1):
    for j in range(i):
        print('*', end="")
    print()
