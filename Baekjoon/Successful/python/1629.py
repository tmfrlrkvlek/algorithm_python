# 1629
A, B, C = map(int, __import__('sys').stdin.readline().strip().split())

def speed_pow(A, M) :
    if M == 0 : return 1
    elif M == 1 : return A % C
    else : return (speed_pow(A, M//2)**2*speed_pow(A, M%2))%C

print(speed_pow(A, B))