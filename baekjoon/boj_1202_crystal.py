import sys
import heapq

N,K = map(int,input().split())
# 가방과 보석 모두 무게순 오름차순 정렬한다.

jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)] # 가장 무게를 적게 담을 수 있는 가방부터.
jewels.sort()
bags.sort()

max_v_heap = [] # 가치기준 최대힙
result = 0

# 해당 방법은 jewels를 이중탐색하지 않고,
# bag과 jewel을 같은 기준으로 정렬을 해두었기 때문에
# bag 턴을 돌 때마다 heap을 초기화 하지 않아도 이전 가방에 들어가는 무게의 보석은 다음 가방에도 무조건 들어가므로 효율적임
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(max_v_heap, -jewels[0][1])
        heapq.heappop(jewels) # 무게를 중심으로 제일 작은게 나간다. (이미 사용한 것과 같음)
    if max_v_heap:
        result -= heapq.heappop(max_v_heap)

print(result)

def overtime():
    N,K = map(int,input().split())
    heap_jewels = []
    for _ in range(N):
        m,v = map(int,input().split())  # 무게, 가치
        heapq.heappush(heap_jewels, (-v,m)) # 정렬기준 : 1. 가치가 높을 수록 (최소 힙이므로 -붙임) 2. 무게가 적을수록.

    bags = sorted([int(input()) for _ in range(K)]) # 가장 무게를 적게 담을 수 있는 가방부터.
    visited_bag = [False] * K
    result = 0

    while heap_jewels:
        v,m = heapq.heappop(heap_jewels)
        for i, bag_m in enumerate(bags):
            if visited_bag[i]:
                continue

            if m <= bag_m :
                visited_bag[i] = True
                result += (-v)
                break

    return result
