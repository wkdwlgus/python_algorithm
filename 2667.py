# 단지 번호 붙이기

import sys

input = sys.stdin.readline
N = int(input())

graph = [list(map(int,input().rstrip())) for _ in range(N)]
dx, dy = [1,0,-1,0], [0,-1,0,1]

def finding_complex(x, y):
    
    stack = [(x, y)]
    cnt = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
                cnt += 1
    return cnt
visited = [[False] * N for _ in range(N)]
total_complex_number = 0
complex_number_list = []    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            total_complex_number += 1
            complex_number_list.append(finding_complex(i, j))

complex_number_list.sort()
print(total_complex_number)
for complex_number in complex_number_list:
    print(complex_number)
    
            
        