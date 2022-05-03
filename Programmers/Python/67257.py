# sol1

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

# sol2
# from itertools import permutations as pm

def solution(expression):
    nums = []
    operators = []
    n = 0
    for c in expression :
        if '0' <= c <= '9' :
            n = n*10 + int(c)
        else :
            nums.append(n)
            n = 0
            operators.append(c)
    nums.append(n)
    result = 0
    for priorities in pm(list(set(operators))) :
        result = max(result, abs(calculator(priorities, nums, operators)))
    return result
    
def calculator(priorities, numbers, operators) :
    def calculateNum(operator, num1, num2) :
        return eval(f'{num1}{operator}{num2}')
    
    def calculateLine(priorities, nums, ops) :
        if not priorities : return nums[0]
        op = priorities[0]
        for idx in range(len(ops)) :
            if ops[idx] == op :
                return calculateLine(priorities, 
                                     nums[:idx]+[calculateNum(op, nums[idx], nums[idx+1])] + nums[idx+2:], 
                                     ops[:idx]+ops[idx+1:])
        return calculateLine(priorities[1:], nums, ops)
                 
    return calculateLine(priorities, numbers, operators)