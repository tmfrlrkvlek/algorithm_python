import heapq

def solution(lines):
    queue = []
    for line in lines :
        date, time, duration = map(str, line.split())
        endDate = list(map(int, date.split("-")))
        endTime = list(map(float, time.split(":")))
        duration = float(duration[:-1]) - 0.001
        startInfo = minus(endDate, endTime, duration)
        heapq.heappush(queue, (startInfo, 0))
        heapq.heappush(queue, (plus(endDate, endTime), 1))
    result = 0
    current = 0
    while queue :
        date = heapq.heappop(queue)
        if date[1] == 0 :
            current += 1
            result = max(result, current)
        else :
            current -= 1
    return result

def minus(date, time, alpha) :
    if time[2] >= alpha :
        return (date, [time[0], time[1], round(time[2]-alpha, 3)])
    elif time[1] > 0 :
        return (date, [time[0], time[1]-1, round(60+time[2]-alpha, 3)])
    elif time[0] > 0 :
        return (date, [time[0]-1, 59, round(60+time[2]-alpha, 3)])
    else :
        return ([2016, 9, 14], [23, 59, round(60+time[2]-alpha, 3)])
    
def plus(date, time) :
    if time[2] < 59.001:
        return (date, [time[0], time[1], round(time[2]+0.999, 3)])
    elif time[1] < 59:
        return (date, [time[0], time[1]+1, round(time[2]+0.999-60, 3)])
    elif time[0] < 59 :
        return (date, [time[0]+1, 0, round(time[2]+0.999-60, 3)])
    else:
        return ([2016, 9, 16], [0, 0, round(time[2]+0.999-60, 3)])