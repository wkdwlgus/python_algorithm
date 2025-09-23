word = input()
word = list(word)

if word == word[::-1]:
    print(1)
else:
    print(0)
# reversed_word = list(reversed(word))
# if word == reversed_word:
#     print(1)
# else:
#     print(0)