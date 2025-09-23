

a, b, c = map(int, input().split())
def mod_pow(a, b, c):
    if b == 0:
        return 
'''
a*a 를 c로 나눈 나머지는 a를 c로 나눈 나머지와 a를 c로 나눈 나머지 두개 곱한걸 c로 나눈 나머지랑 같다.
a**b를 c로 나눈 건 a를 c로 나눈 나머지를 b번 곱하고 c로 나눈 나머지랑 같다.
b를 2등분해서 쪼개서 c로 나눈 나머지끼리 곱한거도 같다. -> 분할정복 아이디어
'''
