import sys
input = sys.stdin.readline
# 입력
N = int(input().rstrip())
status = list(map(int,input().rstrip()))
target = list(map(int,input().rstrip()))

MAX = int(1e9)

def turn(now, i): # int list를 기준으로 1 -> 0 , 0 -> 1 로 바꿔주며, if문으로 index out을 막았다.
    now[i] = 1-now[i]
    now[i-1] = 1-now[i-1]
    if (i+1 < N):
        now[i+1] = 1-now[i+1]
    return now

def turn_switch(status):
    cnt = 0
    now = status[:]
    for i in range(1,N):
        if now[i-1] == target[i-1]:
            continue
        cnt += 1
        now = turn(now, i)

    if now == target:
        return cnt

    return MAX

caseAResult = turn_switch(status)

status[0] = 1 - status[0]
status[1] = 1 - status[1]
result = min(caseAResult, turn_switch(status) + 1)
if result == MAX:
    print(-1)
else:
    print(result)


