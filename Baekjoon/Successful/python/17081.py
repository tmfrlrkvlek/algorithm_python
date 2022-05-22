# 17081
import sys, math
input = sys.stdin.readline

레벨, 체력, 공격력, 방어력 = 1, 20, 2, 2
경험치 = 0
최대_체력 = 20
무기 = 0
방어구 = 0
장신구 = set()

def 상태_출력() :
    print('\n'.join([''.join(line) for line in grid]))
    print(f"Passed Turns : {turn}")
    print(f"LV : {레벨}")
    print(f"HP : {max(0, 체력)}/{최대_체력}")
    print(f"ATT : {공격력}+{무기}")
    print(f"DEF : {방어력}+{방어구}")
    print(f"EXP : {경험치}/{레벨 * 5}")

def 전투로_인해_죽음(몬스터_이름) :
    global x, y, 장신구, 체력
    if 'RE' in 장신구 :
        장신구.remove('RE')
        체력 = 최대_체력
        x, y = 시작_위치
        return
    상태_출력()
    print(f"YOU HAVE BEEN KILLED BY {몬스터_이름}..")
    exit()

def 보스_몬스터_처치() :
    grid[x][y] = '@'
    상태_출력()
    print("YOU WIN!")
    exit()

def 입력이_끝남() :
    grid[x][y] = '@'
    상태_출력()
    print("Press any key to continue.")
    exit()

def 총_방어력() :
    return 방어력+방어구

def 총_공격력() :
    return 공격력+무기

def 레벨업() :
    global 경험치, 레벨, 최대_체력, 공격력, 방어력, 체력
    if 경험치 >= 레벨 * 5 :
        레벨 += 1
        경험치 = 0
        최대_체력 += 5
        공격력 += 2
        방어력 += 2
        체력 = 최대_체력

def 가시함정() :
    global 체력, 장신구
    체력 -= 1 if "DX" in 장신구 else 5
    if 체력 <= 0 :
        전투로_인해_죽음("SPIKE TRAP")

N, M = map(int, input().split())
grid = []
x, y = (0, 0)
K, L = 1, 0
infos = [[[] for _ in range(M)] for _ in range(N)]
for i in range(N) :
    line = input().strip()
    j = line.find('@')
    if j != -1 :
        x, y = (i, j)
    K += line.count("&")
    L += line.count("B")
    grid.append(list(line))
    if j != -1 :
        grid[i][j] = '.'
시작_위치 = (x,y)
S = input().strip()
for _ in range(K) :
    R, C, Name, W, A, H, E = input().split()
    R, C, W, A, H, E = map(int, [R, C, W, A, H, E])
    R, C = R-1, C-1
    infos[R][C] = (Name, W, A, H, E)
for _ in range(L) :
    R, C, T, Opt = input().split()
    R, C = map(int, [R, C])
    R, C = R-1, C-1
    if T != 'O' :
        infos[R][C] = (T, int(Opt)) # W 공격, A 방어
    else :
        infos[R][C] = (T, Opt) # O 장신구
turn = 0
for cmd in S :
    turn += 1
    cmd = ["L", "R", "U", "D"].index(cmd)
    a, b = [(0, -1), (0, 1), (-1, 0), (1, 0)][cmd]
    nx, ny = x+a, y+b
    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
        x, y = nx, ny
    if grid[x][y] == 'B' :
        T, Opt = infos[x][y]
        if T == 'W' :
            무기 = Opt
        elif T == 'A' :
            방어구 = Opt
        else :
            if len(장신구) < 4 :
                장신구.add(Opt)
        grid[x][y] = '.'
    elif grid[x][y] == '^' :
        가시함정()
    elif grid[x][y] in ['&', 'M'] :
        Name, W, A, H, E = infos[x][y] # 이름, 공격력, 방어력, 체력, 경험치
        몬스터_공격 = max(1, W-총_방어력())
        첫_공격_삭제 = 0
        if grid[x][y] == 'M' and "HU" in 장신구 :
            체력 = 최대_체력
            첫_공격_삭제 = 1
        if "CO" in 장신구 :
            배수 = 3 if "DX" in 장신구 else 2
            H -= max(1, 총_공격력()*배수-A)
            if 첫_공격_삭제 > 0 :
                첫_공격_삭제 -= 1
            elif H > 0 :
                체력 -= 몬스터_공격
        내_공격 = max(1, 총_공격력()-A)
        if 첫_공격_삭제 and H - 내_공격 > 0 :
            체력 += 몬스터_공격
        if math.ceil(체력/몬스터_공격) >= math.ceil(H/내_공격):
            체력 -= 몬스터_공격 * max(0, (math.ceil(H/내_공격)-1))
            경험치 += int(E*1.2) if "EX" in 장신구 else E
            레벨업()
            if "HR" in 장신구 :
                체력 = min(최대_체력, 체력+3)
            if grid[x][y] == 'M' :
                보스_몬스터_처치()
            grid[x][y] = '.'
        else :
            체력 = 0
            전투로_인해_죽음(Name)
입력이_끝남()