

def solution(words):
    sorted_words = sorted(words, key = lambda x: (len(x), x))
    for word in sorted_words:
        print(word)
    

N = int(input())

words = []
for i in range(N):
    word = input()
    words.append(word)

solution(words)