# 집합
import sys

input = sys.stdin.readline

M = int(input())

def Add(set_data, n):
    if n not in set_data:
        set_data.add(n)
    else:
        pass


def Remove(set_data, n):
    set_data.discard(n)

def Check(set_data, n):
    return 1 if n in set_data else 0

def Toggle(set_data, n):
    set_data.discard(n) if n in set_data else set_data.add(n)

def All(set_data):
    set_data = {i for i in range(1,21)}
    return set_data

def Empty(set_data):
    set_data = set()
    return set_data

set_data = set()

for _ in range(M):
    order = input().rstrip().split()
    # print(order)
    if order[0] == 'add':
        Add(set_data, int(order[1]))
    elif order[0] == 'remove':
        Remove(set_data, int(order[1]))
    elif order[0] == 'check':
        print(Check(set_data, int(order[1])))
    elif order[0] == 'toggle':
        Toggle(set_data, int(order[1]))
    elif order[0] == 'all':
        set_data = All(set_data)
    elif order[0] == 'empty':
        set_data = Empty(set_data) 
    else:
        pass   


