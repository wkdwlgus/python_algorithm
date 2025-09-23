#색종이

import sys

input = sys.stdin.readline

N = int(input())

data = set()
for _ in range(N):
    x, y = map(int, input().split()) # x: 3, y: 7 / x, y 는 0 ~ 90까지 
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            data.add((j,i))

print(len(data))

