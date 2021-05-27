
def tellJorS(strlist):
    if strlist[0] == '#' and strlist[1] == '0':
        return 0
    else :
        if int(strlist[1]) > 17 or int(strlist[2]) >= 80:
            return strlist[0] + " Senior"
        else:
            return strlist[0] + " Junior"

while (1):
    inputVal = input()

    result = tellJorS(inputVal.split())
    if result:
        print(result)
    else :
        break
