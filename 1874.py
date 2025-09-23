import sys

input = sys.stdin.readline

N = int(input())


box = [i for i in range(N + 1)] # 빼내는 곳
stk = []
now = 1
ans = ''
for _ in range(N):
    num = int(input())
    if num >= now: # num not in stk로 하니까 시간 초과됨
        stk += box[now: num]
        ans += '+\n' * (num - now + 1) + '-\n'
        # res.extend([1]* (num - now + 1) + [0])
        now = num + 1
        
        
    else: # num이 stk에 들어있다면
        if stk[-1] != num:
            print('NO')
            exit()
        else:
            stk.pop()
            ans += '-\n'
print(ans.rstrip())



    


            
            

        

