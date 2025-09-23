#스타트 택시
import sys
from collections import deque

input = sys.stdin.readline

N, M, total_resume = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
ix, iy = map(int, input().split())
ix -= 1
iy -= 1

data = dict()
for i in range(M):
    sx, sy, fx, fy = map(int,input().split())
    sx -= 1
    sy -= 1
    fx -= 1
    fy -= 1
    data[(sx, sy)] = (fx, fy)

s_point = set(data.keys())
dx, dy = [0,-1,0,1], [-1,0,1,0]

def drive_to_end(sx, sy, resume):
    q = deque([(sx, sy)])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    total_resume = 0
    fuel = [[0] * N for _ in range(N)]
    while q:
        v = q.popleft()
        for i in range(4):
            nx, ny = v[0] + dx[i], v[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 1 and not visited[nx][ny]:
                fuel[nx][ny] = fuel[v[0]][v[1]] + 1
                visited[nx][ny] = True
                if fuel[nx][ny] > resume:
                    print(-1)
                    return exit(0)
                else:
                    if (nx, ny) == data[(sx, sy)]:
                        total_resume = (resume - fuel[nx][ny]) + fuel[nx][ny] * 2
                        s_point.discard((sx, sy))
                        return total_resume, nx, ny
                    else:
                        q.append((nx, ny))

    print(-1)
    return exit(0)
                        
def bfs(x, y, oil): # 손님 한명 태우고 도착지까지 데려다주기
    dist = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    found = None # 최초로 찾았을 때의 거리를 표시
    q = deque([(x, y)])
    candidates = []
    while q:
        
        v = q.popleft()
        d = dist[v[0]][v[1]]

        if found is not None and d > found: # 발견 이후 거리가 더 멀어졌을 땐 탐색 중지
            break

        if (v[0], v[1]) in s_point:
            found = d
            candidates.append((v[0],v[1]))
            continue

        if d > oil:
            continue

        for i in range(4):
            nx, ny = v[0] + dx[i], v[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 1 and not visited[nx][ny]:
                dist[nx][ny] = dist[v[0]][v[1]] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
                # 여기에 적어버리면, 4개 내에서 candidates가 추가됨. 실제 동일 거리는 4개보다 많을 수 있음.(당연하게도!)
                # 거리가 같은 애들을 한번에 다 모으려면, 일단 큐에 집어 넣고, popleft를 해서 평가해야함 (16236 아기상어 문제 로직과 비슷함. 참고할 것)
                
                # if dist[nx][ny] > oil:
                #     print(-1)
                #     return exit(0)
                # else: # 연료가 아직 남아있는 경우
                #     if (nx, ny) in s_point: # 손님이 있을 때
                #         # 동일거리 손님들 리스트 만들고, x작은 -> y작은 순으로 해서 손님 확정짓고 초기화하기
                #         candidates.append((nx, ny))
                #         resume = oil - dist[nx][ny]
                #         found = dist[nx][ny]
                #     else:
                #         q.append((nx, ny))

    if candidates:
        candidates.sort()
        sx, sy = candidates[0]
        resume = oil - dist[sx][sy]
        if resume < 0:
            print(-1)
            exit(0)
        return drive_to_end(sx, sy, resume)
    
    print(-1)
    return exit(0)                    
           
while True:
    total_resume, ix, iy = bfs(ix, iy, total_resume)
    if not s_point:
        break

print(total_resume)
    
                 







