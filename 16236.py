#아기 상어

from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

bulk = 2

dx, dy = [0,-1,1,0], [-1,0,0,1]
total_t = 0
exp = 0
def bfs(start):
    global bulk, total_t, exp
    graph[start[1]][start[0]] = 0
    dist =[[-1] * N for _ in range(N)]
    q = deque([start])
    dist[start[1]][start[0]] = 0
    min_dist = None
    candidates = []
    while q:
        x, y = q.popleft()
        if min_dist != None and min_dist < dist[y][x]: # 이미 후보 물고기가 있고, 그 물고기가 현재 이동 거리보다 작은 상황일때는 조사할 필요 없음.
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] <= bulk and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((nx, ny))
                if graph[ny][nx] != 0:
                    if graph[ny][nx] < bulk:

                        if min_dist == None:
                            min_dist = dist[ny][nx]
                            candidates.append((nx, ny))
                        elif min_dist == dist[ny][nx]:
                            candidates.append((nx, ny))
                        else:
                            pass
                        
                    else:
                        pass
                else:
                    pass
    if not candidates:
        return total_t
    else:
        candidates.sort(key = lambda x: (x[1], x[0]))
        total_t += min_dist
        exp += 1
        if exp == bulk: # 경험치 초기화
            bulk += 1
            exp = 0
        return bfs(candidates[0])

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 9:
            start = (j, i)
            break
print(bfs(start))
            
