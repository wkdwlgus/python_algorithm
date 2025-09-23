# 최단경로
# 데이크스트라 기본문제

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split()) # 노드, 간선 개수
K = int(input()) # 시작 노드

graph = [[] for _ in range(V + 1)] # graph의 인덱스: 노드 / 각 리스트: (도착점까지의 거리, 연결된 도착점) 튜플
INF = int(10e9)
dist = [INF] * (V + 1) # dist의 인덱스: 도착지점의 노드 / 각 원소: 해당 인덱스(노드) 까지의 거리 (순회하며 업데이트됨)

# graph 채우기
for _ in range(E):
    u, v, w = map(int, input().split()) # u: 출발점, v: 도착점, w: 거리(가중치)
    graph[u].append((w, v))


def get_short_dist(start):
    dist[start] = 0
    prio_q = []
    heapq.heappush(prio_q, (0, start))
    while prio_q:
        d, v = heapq.heappop(prio_q) # 가장 최단거리 뽑음

        # if dist[v] < d: # 이미 해당 노드에 방문해서 최단거리를 업데이트 한 적이 있다면
        #     continue # 아래 코드 동작 x
            
        for w, end in graph[v]:
            cost = dist[v] + w 
            if cost < dist[end]: # cost: 현재 경로 비용, dist[end]: 현재까지 업데이트된 최단거리
                dist[end] = cost
                heapq.heappush(prio_q, (cost, end))

get_short_dist(K)

for i in range(1, len(dist)):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
