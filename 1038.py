# BOJ 1038
# 감소하는 수
from itertools import combinations
from math import comb as C
'''
최대: 9876543210
C(10,1) + C(10,2) + ... + C(10,10) = 2**10 - 1 = 총 1023 개
'''
N = int(input())

if N >= 1023:
    print(-1)
    exit(0)
    
dec_li = []
for r in range(1, 11):
    for num_tuple in combinations(range(10), r):
        number = int(''.join(map(str, reversed(num_tuple)))) # combinations(오름차순리스트, 뽑는 개수) => 오름차순 튜플이 나옴
        dec_li.append(number)

dec_li.sort()
print(dec_li[N])