# 로프

import sys
input = sys.stdin.readline
N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse= True)

def find_max_weight(ropes):
    
    max_weight = ropes[0]
    partial_ropes = [ropes[0]]
    for i in range(1, len(ropes)):
        partial_ropes.append(ropes[i])
        if ropes[i] * len(partial_ropes) > max_weight:
            max_weight = ropes[i] * len(partial_ropes)

    return max_weight

print(find_max_weight(ropes))

'''
<핵심>
✅ 로프를 추가할때마다 최대 적재 중량이 어떨때 커지는지를 파악하고, 이를 식으로 표현할 수 있어야함.
    - 항상 매 순간마다 최대 적재 중량의 후보는 기존 max 값과 가장 작은 길이의 로프(내림차순 정렬 후 마지막 인덱스로 선택)가 추가되었을 때의 값중 하나임. (둘 중 큰 거)
    - 추가되었을 때의 가능한 최대 적재 중량 값은 무조건 (마지막 로프 * 병렬 연결된 로프의 개수)
✅ 처음 정렬을 한 이유: 정렬을 미리 안해놓으면 매 로프 탐색시 min으로 또 최솟값을 찾아줘야해서 O(N^2) 가 됨

'''