import sys
from collections import deque

input = sys.stdin.readline

N = int(input())



def push(q, n):
    q.append(n)

def pop_left(q):
    if not q:
        return -1
    else:
        n = q.popleft()
        return n

def size(q):
    return len(q)

def isEmpty(q):
    if not q:
        return 1
    else:
        return 0
    
def front(q):
    if not q:
        return -1
    else:
        return q[0]
    
def back(q):
    if not q:
        return -1
    else:
        return q[-1]
    

q = deque([])
for _ in range(N):
    order = input().rstrip()

    if 'push' in order:
        order = order.split(' ')
        push(q, order[1])

    elif order == 'pop':
        print(pop_left(q))
    
    elif order == 'size':
        print(size(q))
    
    elif order == 'empty':
        print(isEmpty(q))
    
    elif order == 'front':
        print(front(q))

    elif order == 'back':
        print(back(q))
    
    else:
        pass
    
