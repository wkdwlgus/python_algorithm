N, M = map(int, input().split())

s1 = set()
s2 = set()
for i in range(N):
    word = input()
    s1.add(word)
for i in range(M):
    word = input()
    s2.add(word)

res = s1 & s2
print(len(res))
for i in res:
    print(i)

# set에는 append가 안된다! 한 원소 추가는 add로 하고, iterable은 list, tuple, set 상관없이 .update(iterable) 로 하면 됨
# a = {}로 하면 dict가 만들어짐. set을 만들고 싶으면 set() 이라고해야함
# set, dict 모두 len() 사용 가능