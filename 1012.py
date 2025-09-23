import sys
from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # M: 열, N: 행, K: 배추개수
    #graph = [[0] * M for _ in range(N)] # M * N 그래프
    visited = [[False] * M for _ in range(N)] # 방문
    

    # 동 남 서 북
    dm = [1, 0 , -1, 0]
    dn = [0, 1, 0, -1]

    bachu = (tuple(map(int, input().split())) for _ in range(K))
    

    def bfs(n, m):
        q = deque([(n, m)])                 
        visited[n][m] = True
        while q:
            n, m = q.popleft()
            for i in range(4):
                nn, nm = n + dn[i], m + dm[i]
                if 0 <= nn < N and 0 <= nm < M:
                    if not visited[nn][nm]:
                        n, m = nn, nm
                        q.append((n, m))
                        visited[n][m] = True
        return 1 # 지렁이 필요 -> 함수 1회 실행

    cnt = 0
    for m, n in bachu:
        if not visited[n][m]:
            cnt += bfs(n, m)
        else:
            continue
    
    print(cnt)