import sys

input = sys.stdin.readline
T = int(input())

def solution(ps):
    cnt = 0
    for i in ps:
        print('i:',i)
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            print(f'{i}:{cnt}')
            if cnt < 0:
                return False
        
    print('result:',cnt)
     
    return True if cnt == 0 else False

for _ in range(T): 
    ps = input()
    if solution(ps):
        print('YES')
    else:
        print('NO')
    