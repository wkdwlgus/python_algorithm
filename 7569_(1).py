#7569 토마토

import sys
from collections import deque

input = sys.stdin.readline


n, m, h = map(int,input().split())
l = m * h
graph = [list(map(int,input().split())) for _ in range(l)]

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, -m, m]
queue = deque([(i,j) for i in range(m * h) for j in range(n) if graph[i][j] == 1])

def bfs():
  while queue:
    v = queue.popleft()
    case = v[0] // m
    for i in range(6):
      ny, nx = v[0] + dy[i], v[1] + dx[i]
      if 0 <= i < 4:
        if case * m <= ny < (case + 1) * m and 0 <= nx < n and graph[ny][nx] == 0:
          graph[ny][nx] = graph[v[0]][v[1]] + 1
          queue.append((ny,nx))
      if i >= 4:
        if 0 <= ny < l and 0 <= nx < n and graph[ny][nx] == 0:
          graph[ny][nx] = graph[v[0]][v[1]] + 1
          queue.append((ny,nx))

def Print():
  for i in graph:
    if 0 in i:
      return print(-1)
  return print(max(map(max,graph)) - 1)

bfs()
Print()