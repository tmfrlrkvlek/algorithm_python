n = int(input())
s = input()
s = list(filter(lambda x: x not in ["J", "A", "V"], list(s)))
if len(s) > 0 :
    print("".join(s))
else :
    print("nojava")