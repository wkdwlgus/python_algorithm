# BOJ 7569
# 토마토(3D)

from collections import deque
import sys

input = sys.stdin.readline

# 방향 벡터: (높이, 행, 열)

dh, dr, dc = [0,0,0,0,1,-1], [0,1,-1,0,0,0], [1,0,0,-1,0,0]

def bfs(box, H, N, M, queue, remain_tmt):
    q = deque(queue)
    last_val = 1  # 박스에 기록되는 마지막 값(=최대 일수 + 1)
    while q:
        h, r, c = q.popleft()
        cur = box[h][r][c]
        for i in range(6):
            nh, nr, nc = h+dh[i], r+dr[i], c+dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = cur + 1 # 박스 그리드에 바로 표시
                last_val = cur + 1 # last_val을 등록하지 않으면 나중에 박스 그리드를 순회하며 최댓값을 찾아야하므로 미리 등록
                remain_tmt -= 1 # 도마도가 익었으니까 줄이자
                q.append((nh, nr, nc))
    return (last_val - 1) if remain_tmt == 0 else -1 # 다 순회했는데 토마토를 익게하지 못할때? 

def main():
    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 3차원 박스
    queue = [(h, n, m) for h in range(H) for n in range(N) for m in range(M) if box[h][n][m] == 1]
    remain_tmt = sum(1 for h in range(H) for n in range(N) for m in range(M) if box[h][n][m] == 0) # (익을 수 있는데) 익지 않은 토마토 개수 (제너레이터)

    # BFS 실행
    if remain_tmt == 0:  # 처음부터 다 익어있으면 탐색할 필요 x
        print(0)
    else:
        print(bfs(box, H, N, M, queue, remain_tmt))
        
main()