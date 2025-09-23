# 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int,input().split()) # 시간, 출력 좌표

init_vi = dict()
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            vi = graph[i][j]
            init_vi[(i, j)] = vi

vi_pt = deque([k for k, v in sorted(init_vi.items(), key = lambda x: x[1])])

dx, dy = [1,0,-1,0], [0,-1,0,1]

t = 0

def bfs(q):
    next_vi = deque([])
    while q:
        vx, vy = q.popleft()
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = graph[vx][vy]
                next_vi.append((nx, ny))
    
    return next_vi

while t < s:
    vi_pt = bfs(vi_pt)
    t += 1
print(graph[x - 1][y - 1])



