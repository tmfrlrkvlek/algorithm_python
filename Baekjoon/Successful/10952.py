while True:
    # n1, n2 = map(int, input().split())
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    sum = n1 + n2
    if sum == 0:
        break
    print(sum)