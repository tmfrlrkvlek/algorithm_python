import re
from itertools import permutations as pm

def calculate(priority, operands, nums) :
    if len(priority) == 0 : return nums[0]
    elif priority[0] not in operands : return calculate(priority[1:], operands, nums)
    else :
        operand = priority[0]
        for idx in range(len(operands)) :
            if operands[idx] == operand :
                if operand == '*' :
                    return calculate(priority, operands[:idx]+operands[idx+1:], nums[:idx]+[nums[idx]*nums[idx+1]]+nums[idx+2:])
                elif operand == '+' :
                    return calculate(priority, operands[:idx]+operands[idx+1:], nums[:idx]+[nums[idx]+nums[idx+1]]+nums[idx+2:])
                elif operand == '-' :
                    return calculate(priority, operands[:idx]+operands[idx+1:], nums[:idx]+[nums[idx]-nums[idx+1]]+nums[idx+2:])

def solution(expression):
    nums = list(map(int, re.compile('[0-9]+').findall(expression)))
    operands = re.compile('[*+-]+').findall(expression)
    operandset = list(set(operands))
    answer = 0
    for priority in pm(operandset) :
        answer = max(answer, abs(calculate(priority, operands, nums)))
    return answer