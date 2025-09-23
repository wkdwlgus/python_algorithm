import sys
from collections import deque

input = sys.stdin.readline

graph = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
rt_graph = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    n, d = rt_graph[i][0] - 1, rt_graph[i][1]
    d_list = [0] * 4
    for j in range(4): # 회전 방향 결정 (아직 회전 확정은 아님. 회전 한다고 했을때의 방향만 결정)
        if j == (n + 2) % 4:
            d_list[j] = d
        else:
            d_list[j] = -d
    
    # 회전 여부 결정
    should_rt = [False] * 4
    should_rt[n] = True
    
    for j in range(n,3):
        if graph[j][2] != graph[j+1][-2] and should_rt[j]:
            should_rt[j+1] = True
    for j in range(n,0,-1):
        if graph[j][-2] != graph[j-1][2] and should_rt[j]:
            should_rt[j-1] = True
           
    for j in range(4):
        if should_rt[j]: # 회전해야한다면
            graph[j].rotate(d)

for i in range(4):
    print(graph[i][0])
res = 0 # 점수 총합
for i in range(4):
    res += graph[i][0]*(2**i)
    
print(res)