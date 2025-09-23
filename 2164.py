from collections import deque

N = int(input())

q = deque([i + 1 for i in range(N)])
while True:
    if len(q) == 1:
        print(q[0])
        break
    n = q.popleft()
    next_n = q.popleft()
    q.append(next_n)

