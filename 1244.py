# 스위치 켜고 끄기

N = int(input()) # 스위치 개수: 1 ~ 100 
state = [i for i in map(int, input().split())]
S = int(input()) # 학생 수: 1 ~ 100

def switch_number(n):
    if n == 1:
        return 0
    else:
        return 1

def male_switch(num, state, N):  
    for i in range(len(state)):
        if (i + 1) % num == 0:
            state[i] = switch_number(state[i])
    return state

def female_switch(num, state, N):
    i = num - 1
    min_val = i - 1
    max_val = i + 1
    state[i] = switch_number(state[i])
    while min_val >= 0 and max_val < len(state):
        if state[min_val] == state[max_val]:
            
            state[min_val] = switch_number(state[min_val])
            state[max_val] = switch_number(state[max_val])
            min_val -= 1
            max_val += 1
        else:
            break
    return state



for _ in range(S):
    sex, num = map(int, input().split()) # 남: 1, 여: 2
    if sex == 1:
        state = male_switch(num, state, N)
    else:
        state = female_switch(num, state, N)

for i in range(len(state)):
    print(state[i], end = ' ' if (i + 1) // 20 == i // 20 else '\n')
    
        


