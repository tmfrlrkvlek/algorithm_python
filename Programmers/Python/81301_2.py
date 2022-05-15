def solution(s):
    num = 0
    nums = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    while s :
        num *= 10
        if '0' <= s[0] <= '9' :
            num += int(s[0])
            s = s[1:]
        else :
            idx = 5
            if s[:2] in ["on", "tw", "si"] :
                idx = 3
            elif s[:2] in ["ze", "fo", "fi", "ni"] :
                idx = 4 
            num += nums[s[:idx]]
            s = s[idx:]
    return num