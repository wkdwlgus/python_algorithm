# 최소 비용 구하기

import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N + 1)]
INF = int(10e9)
dist = [INF] * (N + 1) # 출발점에서 해당 노드까지 거리

# 그래프 그리기
for _ in range(M):
    s, e, d = map(int,input().split())
    graph[s].append((d, e))

start, end = map(int,input().split())

def get_shortest_dist(start, end):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, n = heapq.heappop(q) # 최단거리, 노드 / 힙에서 꺼내지는 순간 해당 노드까지의 거리는 최단거리를 보장함.
        
        if dist[n] < d: # 방문 여부 확인
            continue

        if n == end:
            break # 힙에서 꺼내지는 순간 해당 노드까지의 거리는 최단거리를 보장함.

        for ndist, enode in graph[n]: # 가중치, 도착 노드
            cost = dist[n] + ndist
            if cost < dist[enode]:
                dist[enode] = cost
                heapq.heappush(q, (dist[enode], enode))
    

get_shortest_dist(start,end)

print(dist[end])