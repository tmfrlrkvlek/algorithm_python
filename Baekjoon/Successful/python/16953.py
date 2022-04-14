# 16953
A, B  = map(int, __import__('sys').stdin.readline().strip().split())

def calculate(cur, cnt) :
    if cur == B : return cnt
    elif cur > B : return float('inf')
    else :
        return min(calculate(cur*2, cnt+1), calculate(cur*10+1, cnt+1))

result = calculate(A, 1)
print(result if result < float('inf') else -1)
