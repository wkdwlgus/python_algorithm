# BOJ 9663
# N-Queen
# 완전탐색, 백트래킹
#

# N = int(input())
# # 테이블 초기화
# # 인덱스: 체스판의 행, 각 인덱스의 값: 해당하는 행에서의 퀸의 위치. table[m] = n 은 m행 n열에 퀸이 존재한다는 뜻
# table = [0] * (N + 1) 
# # table = [0, 1, 3, 5]
# def place_queen(r, c): #r행 c열에 퀸을 놓음    
#     global cnt
#     # 트래킹 중단 조건 1 (pruning)
#     for i in range(1, r): # 1행부터 r - 1 행까지의 퀸과 r행의 퀸을 서로 검사하기
#         if table[i] == c or abs(i - r) == abs(table[i] - c):
#                 return
#     table[r] = c
    
#     # 트래킹 중단 조건 2 (끝까지 갔을 때)
#     if r == N:
#         # print(table)
#         cnt += 1
#         return
    
#     for j in range(1, N + 1):
#         r += 1 # 다음 행 탐색 시도
#         place_queen(r, j)
#         r -= 1 # 백트래킹 (종료되면 다시 빼고 다음 열 탐색)
        
    
# cnt = 0
# place_queen(N, 0, 0)
# print(cnt)

# N = int(input())
# table = [0] * N
# cnt = 0

# def place_queen(row):
#     global cnt
    
#     if row == N:
#         cnt += 1
#         return
    
#     for col in range(N):
#         # 현재 위치에 퀸을 놓을 수 있는지 검사
#         valid = True
#         for i in range(row):
#             if table[i] == col or abs(i - row) == abs(table[i] - col):
#                 valid = False
#                 break
        
#         if valid:
#             table[row] = col
#             place_queen(row + 1)

# place_queen(0)
# print(cnt)


# 공간-시간 트레이드오프를 활용
N = int(input())
col = [False] * N  # 열 체크
diag_ru = [False] * (2 * N - 1)  # / 대각선 체크
diag_rd = [False] * (2 * N - 1)  # \ 대각선 체크
cnt = 0

def place_queen(row):
    global cnt
    
    if row == N:
        cnt += 1
        return
    
    for c in range(N):
        if col[c] or diag_ru[row + c] or diag_rd[row - c + N - 1]: # pruning
            continue
            
        col[c] = diag_ru[row + c] = diag_rd[row - c + N - 1] = True
        place_queen(row + 1)
        col[c] = diag_ru[row + c] = diag_rd[row - c + N - 1] = False

place_queen(0)
print(cnt)

N = int(input())
col_set = set()
diag_ru = set() # 오른쪽 위 대각선. r + c 일정
diag_rd = set() # 왼쪽 위 대각선. r - c 일정
cnt = 0
def place_queen(r):
    global cnt
    
    # 종료 조건 (모두 탐색 성공)
    if r == N: 
        cnt += 1
        return
    
    for c in range(N):
        if c in col_set or (r + c) in diag_ru or (r - c) in diag_rd: # 같은 열, 대각선 위치에 이미 queen이 놓여있다면 탐색 x (pruning)
            continue
        
        col_set.add(c)
        diag_ru.add(r + c)
        diag_rd.add(r - c)
        
        place_queen(r + 1)
        
        # pruning 되어 상위 스텝의 함수로 돌아왔으면 놓았던 퀸을 제거 (백트래킹)
        col_set.remove(c)
        diag_ru.remove(r + c)
        diag_rd.remove(r - c)
        
place_queen(0)       
print(cnt)