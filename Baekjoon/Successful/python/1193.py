# 1193

# n = int(input())
# sum = -int((-(8*n-1)**0.5-1)//2)
# order = 0
# if sum == 2 : print("1/1")
# else : 
#     while -int((-(8*(n-order)-1)**0.5-1)//2) == sum : order += 1
    # print(str(order)+"/"+str(sum-order) if sum % 2 else str((sum-order))+"/"+str(+order))

# step = 0  # 현재 몇번째 반복인진
# order = 1 # 현재 규칙의 최대 개수?
# index = 0 # 마지막 인덱스
# n = int(input())
# while True:
#     index += order
#     step += 1
#     if n <= index : break
#     else : order += 4

# now = order - index + n
# max1 = order - (order // 2)
# 분모 = now if now <= max1 else max1 - now%max1
# print(분모)