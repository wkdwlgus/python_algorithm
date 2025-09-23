
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx, dy = [1,0,-1,0], [0,1,0,-1]
def check_chess(chess): # 8*8 리스트가 들어감
    cnt_B = 0
    cnt_W = 0
    
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess[i][j] == 'W':
                        cnt_B += 1
                    else:
                        cnt_W += 1
                else:
                    if chess[i][j] == 'B':
                        cnt_B += 1
                    else:
                        cnt_W += 1
            else:
                if j % 2 == 0:
                    if chess[i][j] == 'B':
                        cnt_B += 1
                    else:
                        cnt_W += 1
                else:
                    if chess[i][j] == 'W':
                        cnt_B += 1
                    else:
                        cnt_W += 1
  
    #     for j in range(8):
    #         x, y = j, i
    #         for k in range(4):
    #             nx, ny = x + dx[k], y + dy[k]
    #             if 0 <= nx < 8 and 0 <= ny < 8:
    #                 if chess[x][y] == chess[nx][ny]:
    #                     chess[nx][ny] = 'W' if chess[nx][ny] == 'B' else 'B'
    #                     cnt += 1
    return min(cnt_W, cnt_B)

ans = 10**2

# chess = [list(graph[i][1:1+8]) for i in range(1,1+8)]
# print(chess)
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        chess = [list(graph[i][j:j+8]) for i in range(i,i+8)] #2차원 그래프 자르기
       
        cnt = check_chess(chess)
        ans = min(ans, cnt)
        if ans == 0:
            print(0)
            exit(0)
print(ans)
            
