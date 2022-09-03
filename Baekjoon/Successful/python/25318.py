import sys
input = sys.stdin.readline
N = int(input().strip())
if N == 0 :
    print(N)
    exit(0)
T = []
L = []
D = 24*60*60
M = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
for _ in range(N) :
    date, time, l = map(str, input().strip().split())
    date = list(map(int, date.split('/')))
    time = list(map(int, time.split(':')))
    day = 1 if date[0] > 2020 or (date[0] == 2020 and date[1] > 2) else 0
    day += (date[0]-2019)*365 + M[date[1]] + date[2]
    time = time[0]*60*60 + time[1]*60 + time[2] 
    day += time/D
    T.append(day)
    L.append(int(l))
Tn = T[-1]
P = [max(0.5**((Tn-T[i])/365), 0.9**(N-i-1)) for i in range(N)]
Psum = 0
PLsum = 0
for i in range(N):
    Psum += P[i]
    PLsum += P[i]*L[i]
result = round(PLsum/Psum)
print(result)
