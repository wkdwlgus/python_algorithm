#내리막 길

import sys

input = sys.stdin.readline

M, N = map(int, input().split())

stairs = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)] # -1 이라면 아직 방문 안한 상태, 0 이라면 해당 지점에서 도착 지점까지 갈 수 있는 경로가 0개

dm, dn = [0, 1, 0, -1], [-1, 0, 1, 0]
def dfs(m, n):
    if m == M - 1 and n == N - 1:
        return 1
    
    if dp[m][n] != -1: # 방문한 적이 있을 경우 깊이 탐색 안함 (메모이제이션)
        return dp[m][n]
    
    else: dp[m][n] = 0 # 해당 지점 첫 방문시 (해당 지점에서부터 탐색 시작)

    # 첫 방문시 탐색
    for i in range(4):
        nm, nn = m + dm[i], n + dn[i]
        if 0 <= nm < M and 0 <= nn < N and stairs[nm][nn] < stairs[m][n]:
            dp[m][n] += dfs(nm, nn) # 탐색 실행
    
    return dp[m][n]

                
print(dfs(0,0))
            
