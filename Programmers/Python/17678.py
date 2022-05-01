def solution(n, t, m, timetable):
    timetable = sorted([time_to_num(time) for time in timetable])
    available = 0
    N = 0; time = 540
    customers = [0 for _ in range(n)]
    for p in timetable :
        if N >= n : break
        elif p <= time :
            if customers[N] < m : 
                available = p-1
                customers[N] += 1
            elif customers[N] == m : 
                N += 1
                time += t
                if N < n : 
                    available = p-1
                    customers[N] += 1
        else :
            if customers[N] < m : 
                available = time
            while p > time and N < n:
                N += 1
                time += t
            if N < n : 
                available = p-1
                customers[N] += 1
    if customers[-1] < m : available = 540 + (n-1)*t
    return num_to_time(available)

def time_to_num(time) :
    h, m = map(int, time.split(':'))
    return h*60 + m

def num_to_time(time) :
    return '{:02d}:{:02d}'.format(time//60, time%60)