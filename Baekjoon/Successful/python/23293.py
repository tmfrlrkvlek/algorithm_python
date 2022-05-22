# 23293
import sys
input = sys.stdin.readline
T, N = map(int, input().split())
negative_logs = []
negative_players = set()
players_loc = [1 for _ in range(N+1)]
players_items = [[] for _ in range(N+1)]
for _ in range(T):
    log = list(input().split())
    action_code = log.pop(2)
    if action_code == 'C' :
        log_num, player_num, action_num1, action_num2 = map(int, log)
    else :
        log_num, player_num, action_num = map(int, log)
    if action_code == 'M' :
        players_loc[player_num] = action_num
    elif action_code == 'F' :
        if players_loc[player_num] != action_num :
            negative_logs.append(log_num)
        players_items[player_num].append(action_num)
    elif action_code == 'C' :
        is_available = True
        if action_num1 in players_items[player_num] :
            players_items[player_num].remove(action_num1)
        else :
            is_available = False
        if action_num2 in players_items[player_num] :
            players_items[player_num].remove(action_num2)
        else :
            is_available = False
        if not is_available:
            negative_logs.append(log_num)
    elif action_code == 'A' :
        if players_loc[action_num] != players_loc[player_num] :
            negative_logs.append(log_num)
            negative_players.add(player_num)
print(len(negative_logs))
if negative_logs :
    print(' '.join(map(str, sorted(negative_logs))))
print(len(negative_players))
if negative_players :
    print(' '.join(map(str, sorted(list(negative_players)))))