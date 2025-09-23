import sys

input = sys.stdin.readline

T = int(input())
card_number = []
for i in range(T):
    num = input().rstrip()
    card_number.append(num)

for card in card_number:
    sum = 0
    for i, v in enumerate(card): # index와 Value가 같이 필요하면 enumerate 사용하기
        num = int(v)
        if (i+1) % 2 != 0:
            nnum = num * 2
            if nnum >= 10:
                num = nnum // 10 + nnum % 10
            else:
                num = nnum
        print(num, i)
        sum += num
    print(sum)
    if sum % 10 == 0:
        print('T')
    else:
        print('F')
        