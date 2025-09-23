import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 보드 크기(N*N)
K = int(input()) # 사과 개수
loc = {(x - 1, y - 1) for _ in range(K) for x, y in [tuple(map(int,input().split()))] } # 사과 위치
L = int(input()) # 방향 변환 횟수
d_info = [[int(t), d] for t,d in (input().split() for _ in range(L)) ] # 방향 변환 정보

total_t = d_info[0][0]
for i in range(1,L):
    d_info[i][0] = d_info[i][0] - total_t
    total_t += d_info[i][0]






snake = deque()
x, y = (0, 0)
snake.append((x, y)) # 현재 위치
time = 1 # 최소 1초임
# 동, 남, 서, 북

dx, dy = [0,1,0,-1], [1,0,-1,0]
c_idx = 0 # 처음엔 서쪽


is_done = False
while True:

    if is_done:
        break
    for i in range(L):
        for j in range(d_info[i][0]): # 몇초동안 진행하는지
            nx, ny = x + dx[c_idx], y + dy[c_idx]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snake: # 갈 수 있으면
                time += 1
                snake.append((nx, ny))
                if (nx, ny) in loc:
                    loc.remove((nx, ny))
                
                else:
                    snake.popleft()
                x, y = nx, ny
            else:
                is_done = True
                break
        
        if is_done:
            break
            
        if d_info[i][1] == 'L':
            c_idx = (c_idx -1) % 4 # 왼쪽으로 90도 회전
        else:
            c_idx = (c_idx + 1) % 4 # 오른쪽으로 90도 회전

    while not is_done:
        nx, ny = x + dx[c_idx], y + dy[c_idx]
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in snake: # 갈 수 있으면
            time += 1
            snake.append((nx, ny))
            if (nx, ny) in loc:
                loc.remove((nx, ny))
            
            else:
                snake.popleft()
            x, y = nx, ny
        else:
            is_done = True
            break

    if is_done:
        break

print(time)


