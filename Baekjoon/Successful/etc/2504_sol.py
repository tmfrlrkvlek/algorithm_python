# 2504

iv = list(input())
stack = []
error = 0
if iv.count('(') != iv.count(')') or iv.count('[') != iv.count(']'): print(0)
else : 
    sum = []
    for i in iv :
        if i == ')' or i == ']':
            val = 2
            v1 = '('
            v2 = '['
            if i == ']' : 
                val = 3
                v1 = '['
                v2 = '('
            t = 0
            while stack :
                top = stack.pop(-1)
                if top == v1:
                    if t == 0:
                        stack.append(val)
                    else:
                        stack.append(val * t)
                    break
                elif top == v2:
                    error = 1
                    break
                else :
                    t = t + top
        else:
            stack.append(i)
    if error : print(0)
    else:
        s = 0
        for i in stack :
            s += i
        print(s)

