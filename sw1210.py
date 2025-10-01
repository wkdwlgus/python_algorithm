
# 사다리 문제

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dx , dy = [0, 0, 1], [1, -1, 0] # 우, 좌, 아래순
def finding_arrived_point(x, y,visited, graph, n):
    if x == n - 1:
        return graph[x][y]
    
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0 and not visited[nx][ny]:
            visited[x][y] = True
            return finding_arrived_point(nx, ny, visited, graph, n)
            
        
def finding_arrived_point_ladder(x, y, graph, n):
    if x == n - 1:
        return graph[x][y]
    
    if y > 0 and graph[x][y-1] == 1: 
        while y > 0 and graph[x][y -1] == 1:
            y -= 1
        
    elif y < n - 1 and graph[x][y + 1] == 1: 
        while y < n - 1 and graph[x][y + 1] == 1:
            y += 1
    
    return finding_arrived_point_ladder(x + 1, y, graph, n)

n = 100
for test_case in range(1, 11):
    T = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    for y in range(n):
        if graph[0][y] == 1:
            # visited = [[False] * n for _ in range(n)]
            # visited[0][y] = True
            # result = finding_arrived_point(0, y, visited, graph, n)
            # if result == 2:
            #     print(f'#{test_case}', y)
            #     break
            result = finding_arrived_point_ladder(0, y, graph, n)
            if result == 2:
                print(f'#{test_case}', y)
                break
            