# 방 번호
# from collections import Counter
from math import ceil

N = input().replace('9','6')

'''
c = Counter(N)
c['6'] = ceil(c['6'] / 2)
c_max = c.most_common(1)
print(c.most_common(1)[0][1])
'''

counter = [0] * 10 # 숫자 카운트 정보를 담는 리스트를 이렇게도 만들 수 있음

for i in N:
    n = int(i)
    counter[n] += 1

counter[6] = ceil((counter[6] + counter[9]) / 2)
counter[9] = 0

print(max(counter))

