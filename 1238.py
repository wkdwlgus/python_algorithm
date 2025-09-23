# 파티

import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reversed_graph = [[] for _ in range(N + 1)]
INF = int(1e9)
# 그래프 만들기
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e)) # 돌아올때 사용
    reversed_graph[e].append((t, s)) # 파티 갈때 사용

def go_to_party(start, N): # i, X
    go_dist = [INF] * (N + 1)
    go_dist[start] = 0
    q = []
    heapq.heappush(q,(0, start))
    while q:
        d, n = heapq.heappop(q)
        if d > go_dist[n]:
            continue
        for w, next_node in reversed_graph[n]:
            cost = go_dist[n] + w
            if cost < go_dist[next_node]:
                go_dist[next_node] = cost
                heapq.heappush(q,(go_dist[next_node], next_node))

    return go_dist


def go_back_home(end, N): # X, i
    back_dist = [INF] * (N + 1)
    back_dist[end] = 0
    q = []
    heapq.heappush(q,(0, end))
    while q:
        d, n = heapq.heappop(q)
        if d > back_dist[n]:
            continue
        for w, next_node in graph[n]:
            cost = back_dist[n] + w
            if cost < back_dist[next_node]:
                back_dist[next_node] = cost
                heapq.heappush(q,(back_dist[next_node], next_node))
        
    return back_dist

go_dist = go_to_party(X, N)
back_dist = go_back_home(X, N)

total_dist = [go_dist[i] + back_dist[i] for i in range(1, N + 1) if go_dist[i] != INF and back_dist[i] != INF] # for + if + append 의 결합
print(max(total_dist))
'''
answer = 0
for i in range(1, N + 1):
    if go_dist[i] != INF and back_dist[i] != INF:
        answer = max(answer, go_dist[i] + back_dist[i])

print(answer)
'''
