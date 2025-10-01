# BOJ 9466
# 텀 프로젝트

import sys

input = sys.stdin.readline

T = int(input())

def make_group(i):
    global cnt
    path = []
    while grouped[i] == 0: # 사이클 찾을때까지 탐색 (돌아올때까지 탐색)
        grouped[i] = 1 # 탐색 중
        path.append(i)
        i = graph[i]
        
    if grouped[i] == 1: # 사이클 발견한 경우
        start_idx = path.index(i)
        length = len(path) - start_idx
        cnt += length
    
    for j in path: 
        grouped[j] = 2 # 탐색 완료 표시
        

            

for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    grouped = [0] * (n + 1) # 0: 탐색 전, 1: 탐색 중, 2: 탐색 후
    cnt = 0
    for i in range(1, n + 1):
        if not grouped[i]: # 탐색 전이라면,
            make_group(i)
    print(n - cnt)
    
    