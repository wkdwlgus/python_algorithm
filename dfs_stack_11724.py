import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1) # 방문 체크

# 그래프 제작
for _ in range(M):
    u, v = map(int, input().split()) # 양 끝점
    graph[u].append(v)
    graph[v].append(u)
    

def dfs_stack(start, graph, visited):
    visited[start] = True
    stack = [start]
    while stack:
        x = stack.pop() # x번 노드에 연결된게 2, 3 이라 치면
        for i in graph[x]: # [2, 3]
            if not visited[i]:
                stack.append(i) # 방문 스택 쌓기
                visited[i] = True # 방문처리
    return 1

def dfs_recursion(start, graph, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs_recursion(i, graph, visited)
    return 1
            
    
    
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += dfs_recursion(i, graph, visited)
        
print(cnt)
