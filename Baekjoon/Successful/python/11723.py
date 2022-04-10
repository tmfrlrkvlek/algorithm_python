# 11723
import sys
input = sys.stdin.readline
S = set()

def add(x) :
    S.add(x)

def remove(x) :
    S.discard(x)

def check(x) :
    print(1 if x in S else 0)

def toggle(x) :
    if x in S : S.discard(x)
    else : S.add(x)

def all() :
    global S
    S = set(range(1, 21))

def empty() :
    global S
    S = set()

for _ in range(int(input().strip())) :
    command = input().strip().split()
    line = command[0]
    if len(command) == 1 :
        if line == "all" : all()
        elif line == "empty" : empty()
    else :
        x = int(command[1])
        if line == "add" : add(x)
        elif line == "remove" : remove(x)
        elif line == "check" : check(x)
        elif line == "toggle" : toggle(x)