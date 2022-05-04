# 64063

import sys
sys.setrecursionlimit(10**8)

def solution(k, room_number):
    def find(num, empty_room) :
        if num not in empty_room :
            empty_room[num] = num+1
            return num
        number = find(empty_room[num], empty_room)
        empty_room[num] = number
        return number
    answer = []
    empty_room = {}
    for num in room_number :
        number = find(num, empty_room)
        answer.append(number)
    return answer