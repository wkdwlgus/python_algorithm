# 수 묶기

'''
    ex)
    -10 -3 -1 0 2 5 -> 40
    -10 -3 0 2 3 5 -> 47
    -10 -5 0 1 2 -> 53
    -10 -5 2 3 5 -> 67
    -5 0 1 -> 1
    -5 1 -> -4
    -10 -3 -1 0 1 2 3 -> 37
    5 4 3 1 1 -> 9 + 4 + 1 = 14

    음수가 짝수개이면 다 곱함.
    음수가 홀수개이면
        0이 있다면 제일 0에 가까운 음의 값이랑 0이랑 곱하기
        0이 없다면 
        -5 -2 -1 3 5
        0에 가까운 음의 값은 묶지 않기
    양수에 1이 있다면 1은 묶지 않음.
    음 수열 양 수열 길이 1일때 분리
'''

def binding_seq(seq):
    minus_seq = sorted([i for i in seq if i < 0])
    plus_seq = sorted([i for i in seq if i > 0], reverse=True)
    len_minus = len(minus_seq)
    len_plus = len(plus_seq)
    if len_minus > 1:
        if len_minus % 2 == 0:
            minus_res = [a * b for a, b in zip(minus_seq[::2], minus_seq[1::2])]
        else:
            if 0 in seq:
                minus_res = [a * b for a, b in zip(minus_seq[::2], minus_seq[1::2])]
            else:
                minus_res = [a * b for a, b in zip(minus_seq[::2], minus_seq[1::2])] + [minus_seq[-1]]
    elif len_minus == 1:
        if 0 in seq:
            minus_res = [0]
        else:
            minus_res = minus_seq
    else:
        minus_res = [0]

    if len_plus > 1:
        if len_plus % 2 == 0:
            plus_res = [a * b if a != 1 and b != 1 else a + b for a, b in zip(plus_seq[::2], plus_seq[1::2])]
        else:
            plus_res = [a * b if a != 1 and b != 1 else a + b for a, b in zip(plus_seq[::2], plus_seq[1::2])] + [plus_seq[-1]]
    elif len_plus == 1:
        plus_res = plus_seq
    else:
        plus_res = [0]
    
    return sum(minus_res) + sum(plus_res)
        
    

        


N = int(input())
sequence = [int(input()) for _ in range(N)]

print(binding_seq(sequence))





