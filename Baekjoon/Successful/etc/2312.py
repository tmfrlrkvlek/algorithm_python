n = int(input())

for i in range(n):
    num = int(input())
    cp = num
    primeNum = []
    countNum = []
    devideNum = 2
    while (cp != 1):
        if (cp % devideNum == 0) :
            if devideNum not in primeNum :
                primeNum.append(devideNum)
                countNum.append(1)
            else:
                countNum[primeNum.index(devideNum)] += 1
            cp = cp /devideNum
        else:
            if devideNum == 2 :
                devideNum = 3
            else :
                devideNum += 2
    for idx in range(len(primeNum)):
        print(primeNum[idx], countNum[idx])