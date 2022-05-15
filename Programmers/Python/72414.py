# 72414
# 미완

def solution(play_time, adv_time, logs):
    def time_to_int(time) :
        h, m, s = map(int, time.split(':'))
        return h*60*60 + m*60 + s
    
    def int_to_time(time) :
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        return "{:02d}:{:02d}:{:02d}".format(h, m, s)
    
    timeline = [0] * (time_to_int(play_time)+1)
    adv_time = time_to_int(adv_time)
    
    for log in logs :
        start, end = map(time_to_int, log.split('-'))
        for i in range(start, end+1) :
            timeline[i] += 1
            
    answer = 0
    current = sum(timeline[:adv_time+1])
    max_log = current
    for i in range(1, len(timeline)-adv_time) :
        current += timeline[i+adv_time]
        current -= timeline[i-1]
        if max_log < current :
            max_log = current
            answer = i
    
    return int_to_time(answer)