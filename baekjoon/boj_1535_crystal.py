# dfs 방법
N = int(input()) # 사람의 수
strength = list(map(int,input().split())) # 잃는 체력
happiness = list(map(int,input().split())) # 얻는 기쁨

result = 0 # 인사 못하면 기쁨은 0으로 반환된다.
def dfs(cur_strength, cur_happiness, idx):
    global result
    if cur_strength >= 100:
        return
    if idx >= N:
        result = max(result, cur_happiness)
        return
    dfs(cur_strength + strength[idx], cur_happiness + happiness[idx], idx+1) # 현재 idx의 사람에게 인사한다.
    dfs(cur_strength, cur_happiness, idx+1) # 인사 안 한다.


dfs(0,0,0)
print(result)


# dp 방법
N = int(input())
lst = list(zip(map(int, input().split()), map(int,input().split())))
lst.sort(reverse=True) # value 기준 내림차순

dp = {0:0} # key = 기쁨(value), value = key를 만들기 위한 체력(weight)

# (w,v) 조합을 탐색하며 dp 업데이트하며 dp는 현재 가치 합 -> 최소무게를 저장
for weight, value in lst:
    data = {}
    for v,w in dp.items():
        v += value
        w += weight

        if dp.get(v, 100) > w: # 같은 value를 가지는데 지금 weight가 기존 dp것보다 작으면 update한다.
            data[v] = w
    dp.update(data)

print(max(dp.keys()))
