# 인구 이동
import sys
from collections import deque

input = sys.stdin.readline


N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(r, c, L, R, N):
    
    union = [(r, c)]
    total = graph[r][c]
    visited[r][c] = True
    q = deque([(r, c)])
    while q:
        v = q.popleft()
        for i in range(4):
            nr, nc = v[0] + dr[i], v[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N and L <= abs(graph[nr][nc] - graph[v[0]][v[1]]) <= R and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
                union.append((nr, nc)) # 나중에 연합국들의 graph 인구수를 수정해줘야하므로 union 리스트가 필요함 (나중에 union으로 반복문 돌려서 graph 인구수 수정)
                total += graph[nr][nc]
    return union, total # 연합국 좌표 리스트, 인구수 총합

    

        
day = 0
while True:
    moved = False # 하루마다 이동 여부 초기화
    visited = [[False] * N for _ in range(N)] # 하루마다 visited 초기화
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: 
                union, total = bfs(i, j, L, R, N)
                if len(union) >= 2:
                    moved = True # 하루동안 이동함
                    for r, c in union: # 연합국끼리 인구수 같아짐 (인구이동)
                        graph[r][c] = total // len(union)
                      
    
    if not moved:
        break

    day += 1 # 이동이 없어 종료되는 날은 day += 1 이 작동안해야하므로 if not moved 뒤에 배치

print(day)

