# Z

N, r, c = map(int, input().split())


def z(n, r, c):
    if n == 0:
        return 0
    half = 1 << n - 1 # n = 3 이면 half는 2^2 = 4
    quat_val = half * half
    if r < half and c < half: # 1 사분면
        return z(n - 1, r, c)
    elif r < half and c >= half: # 2 사분면
        return quat_val + z(n - 1, r, c - half)
    elif r >= half and c < half: # 3 사분면
        return quat_val * 2 + z(n - 1, r - half, c)
    elif r >= half and c >= half: # 4 사분면
        return quat_val * 3 + z(n - 1, r - half, c - half)
    
print(z(N, r, c))

    
