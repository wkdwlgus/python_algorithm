# 단어뒤집기

strings = input()


# 풀이 2
def reverse_words_with_tags(s):
    result = [] #변경된 문자열을 담는 리스트
    i = 0
    while len(s) > i:
        if s[i] != '<': # 단어 일때
            j = i
            while len(s) > j and s[j] != '<':
                j += 1  # 태그 전까지의 단어 인덱스 체크
            
            words = s[i: j].split(' ')
            reversed_words = [word[::-1] for word in words]
            result.append(' '.join(reversed_words))

            i = j

        else: # 태그 일때
            j = i
            while j < len(s) and s[j] != '>':
                j += 1
            result.append(s[i: j + 1])
            i = j + 1
    return ''.join(result)

print(reverse_words_with_tags(strings))

    








# 풀이 1
'''
state = None
total_li = []
i = 0
while i < len(strings):

    if strings[i] == '<':
        state = 'tag'
        total_li.append(strings[i]) # '<'
        

    else:
        if state == 'tag':
            s = strings.find('>', i)
            tag_li = strings[i: s]
            total_li.extend(tag_li)
            total_li.append('>')
            state = None
        
        else: # 그냥 문자가 왔고, 태그모드가 아닐 때
            state = 'word'
            s = strings.find('<', i)
            if s == -1:
                words = strings[i:].split(' ')
                 
            else:
                words = strings[i:s].split(' ')

            for j in range(len(words)):
                total_li.extend(words[j][::-1])
                if j != len(words) - 1:
                    total_li.append(' ')
                else:
                    continue
            state = None  
    
    i = len(total_li)
            
    
print("".join(total_li))
'''
                    
                


        






