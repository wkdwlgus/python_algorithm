# BOJ 12100
# 2048 (Easy)

'''
무조건 현재 상황에서 크게 합치는게 최선의 방법인가? -> 보장할 수 없다. 이게 보장되면 그리디 풀이 가능
5층까지 완전 탐색 -> 
2**1, 2**2, 2**10 등이 들어감
1<=N<=20
'''

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]



