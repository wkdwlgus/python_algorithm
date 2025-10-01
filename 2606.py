# 바이러스

import sys

input = sys.stdin.readline

N = int(input())
l = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def count_virus(n):
    cnt = 0
    stack = [n]
    visited[n] = True
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1
    return cnt

print(count_virus(1))
    