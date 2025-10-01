import sys

input = sys.stdin.readline

T = int(input())

dx, dy = [1,0,-1,0], [0,-1,0,1]
def finding_cabbage(x, y, visited):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                
    return 1

for _ in range(T):
    M, N, K = map(int,input().split()) # 가로길이, 세로길이
    
    # graph 만들기
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt += finding_cabbage(i, j, visited)
    print(cnt)
                
    
    
    