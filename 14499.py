# 주사위 굴리기
import sys
from collections import deque

'''
  2
 4136
  5
  6

남쪽회전
  6
 4235
  1
  5

동쪽회전
  6
 5423
  1
  3
'''

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

ud = deque([0,0,0,0]) # idx 0: 뒷면, idx 1: 하늘면, idx 2: 앞면, idx 3: 바닥면
rl = deque([0,0,0,0]) # idx 0: 왼쪽면, idx 1: 하늘면, idx 2: 오른쪽면, idx 3: 바닥면

def rotate_dice(n):
    if n == 1:
       rl.rotate(1)
       ud[3] = rl[3]
       ud[1] = rl[1]
    elif n == 2:
       rl.rotate(-1)
       ud[3] = rl[3]
       ud[1] = rl[1]
    elif n == 3:
       ud.rotate(-1)
       rl[3] = ud[3]
       rl[1] = ud[1]
    elif n == 4:
       ud.rotate(1)
       rl[3] = ud[3]
       rl[1] = ud[1]
    else: pass

# dx dy 만들기
dx, dy = [0,0,0,-1,1], [0,1,-1,0,0]
for n in order:
    nx, ny = x + dx[n], y + dy[n]
    if 0 <= nx < N and 0 <= ny < M:
       rotate_dice(n)
       if graph[nx][ny] == 0: # 바닥숫자가 0이라면 주사위 -> 칸 복사
          graph[nx][ny] = ud[3]
          
       else: # 바닥 숫자가 0이 아니라면 칸 -> 주사위 복사
          ud[3], rl[3] = graph[nx][ny], graph[nx][ny]
          graph[nx][ny] = 0 # 칸에 쓰여있는 수는 0이 됨
        
       x, y = nx, ny
       print(ud[1])


