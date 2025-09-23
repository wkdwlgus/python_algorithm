# 숨바꼭질 3
import heapq
from collections import deque

# 0 - 1bfs

N, K = map(int,input().split())
INF = int(1e9)
dist = [INF] * (int(1e5) + 1)
def bfs(start, end):
    q = deque() # (node, time)
    q.append((start, 0))
    dist[start] = 0
    while q:
        n, t = q.popleft()

        if dist[n] < t:
            continue

        if n == end:
            return dist[n]
        candidate = [(n + 1, 1), (n - 1, 1), (n * 2, 0)]


        for i, w in candidate:
            if 0 <= i <= 100_000:
                cost = dist[n] + w
                if cost < dist[i]:
                    dist[i] = cost
                    if w == 0:
                        q.appendleft((i, dist[i]))
                    else:
                        q.append((i, dist[i]))



print(bfs(N, K))


# 데이크스트라
'''
N, K = map(int,input().split())
INF = int(1e9)
time = [INF] * (int(1e5) + 1)

def get_shortest_time(start, end):
    time[start] = 0
    q = []
    heapq.heappush(q,(0, start))

    while q:
        t, node = heapq.heappop(q)

        if t > time[node]: # 방문 여부 확인
            continue

        if node == end:
            break

        candidate = [(1, node - 1), (1, node + 1), (0, node * 2)]
        for w, next_node in candidate:
            cost = time[node] + w
            if 0 <= next_node < len(time) and cost < time[next_node]: # cost가 현재 최단시간보다 더 작으면 업데이트 필요
                time[next_node] = cost
                heapq.heappush(q,(time[next_node], next_node))

get_shortest_time(N,K)


print(time[K])
'''
