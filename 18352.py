# 특정 거리의 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)

def bfs(n):
    dist = 0
    visited = [False] * (N + 1)
    visited[n] = True
    cities = []
    q = deque([(n, dist)])
    while q:
        v = q.popleft()
        if v[1] >= K:
            if v[1] == K:
                cities.append(v[0])
                continue
            else:
                break # 굳이 else break를 안걸어도, continue가 확장을 막아줘서 괜찮음.
        for i in graph[v[0]]:
            if not visited[i]:
                q.append((i, v[1] + 1))
                visited[i] = True
    
    return sorted(cities)

cities = bfs(X)

if not cities:
    print(-1)

else:
    for i in cities:
        print(i)
    



