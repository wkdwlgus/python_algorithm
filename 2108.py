#통계학
import sys
from collections import Counter


input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

def mean(data): # 평균
    return round(sum(i for i in data) / len(data))

def median(data): # 중앙값
    data.sort()
    idx = int((len(data) - 1) / 2)
    return data[idx]

'''

def mode(data): # 최빈값
    if len(data) == 1:
        return data[0]
    data_set = set(data)
    data_dict = {i: 0 for i in data_set}
    for i in data:
        data_dict[i] += 1
    sorted_data = sorted(list(data_dict.items()), key = lambda x: (-x[1],x[0]))
    if sorted_data[0][1] == sorted_data[1][1]:
        return sorted_data[1][0]
    else: 
        return sorted_data[0][0]
'''

def mode(data):
    if len(data) == 1:
        return data[0]
    
    else:
        cnt_data = Counter(data).most_common()
        max_freq = cnt_data[0][1]
        candidate = [num for num, freq in cnt_data if max_freq == freq]
        candidate.sort()
        return candidate[0] if len(candidate) == 1 else candidate[1]


def rng(data): # 범위(range)
    return max(data) - min(data)


print(mean(data))
print(median(data))
print(mode(data))
print(rng(data))
    