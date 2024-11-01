# 2156

n = int(input())
glasses = [[0, 0, 0] for _ in range(n)]
for i in range(n) :
    fill = int(input())
    if i == 0 :
        glasses[i] = [0, fill, fill]
    elif i == 1 :
        glasses[i] = [max(glasses[i-1]), max(glasses[i-1][1], fill), max(glasses[i-1][:2]) + fill]
    else :
        glasses[i] = [max(glasses[i-1]), 
                      glasses[i-1][0] + fill,
                      glasses[i-1][1] + fill]
print(max(glasses[-1]))