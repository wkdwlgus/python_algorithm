# 요세푸스 문제 0

N, K = map(int,input().split())

def solution(N, K):
    table = [str(i) for i in range(1, N + 1)]
    res = []
    idx = -1
    for n in range(N):
        idx = (idx + K) % len(table)
        num = table[idx]
        res.append(num)
        table.pop(idx)
        idx -= 1
        
    return res

print('<' + ', '.join(solution(N, K)) + '>')