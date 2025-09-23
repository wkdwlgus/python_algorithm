
import sys

input = sys.stdin.readline


N = int(input().rstrip())

stk = []

for _ in range(N):
    order = input().rstrip()
    if 'push' in order:
        order = order.split(' ')
        n = order[1]
        stk.append(n)
    elif order == 'pop':
        if not stk: # 빈 리스트 확인법
            print(-1)
        else:
            n = stk.pop()
            print(n)

    elif order == 'size':
        print(len(stk))

    elif order == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)

    else: pass