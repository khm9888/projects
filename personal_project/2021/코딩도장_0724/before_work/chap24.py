# table = str.maketrans('aeiou', '12345')
# 'apple'.translate(table)
# # '1ppl2'

# x=' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# print(x)
# # 'apple pear grape pineapple orange'

# #구두점 삭제하기

# import string
# print(', python.'.strip(string.punctuation))
# # ' python'
# print(string.punctuation)
# #'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# #정렬하기

# print('python'.ljust(10)), #str.ljust , rjust, center
# # 'python    '

# 문자열 왼쪽에 0 채우기

# >>> '35'.zfill(4)        # 숫자 앞에 0을 채움
# '0035'
# >>> '3.5'.zfill(6)       # 숫자 앞에 0을 채움
# '0003.5'
# >>> 'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음
# '00000hello'

# 문자열 찾기

# >>> 'apple pineapple'.find('pl')
# 2
# >>> 'apple pineapple'.find('xy')
# -1

# 문자열 찾기(오른쪽)


# >>> 'apple pineapple'.rfind('pl')
# 12
# >>> 'apple pineapple'.rfind('xy')
# -1

##index //rindex 도 있지만, 값이 없을 경우 error 발생시킨다.

# 문자열- 길이

# >>> '%10s' % 'python'
# '    python'

# >>> f'{"hi":<10}'  # 왼쪽 정렬
# 'hi        '
# >>> f'{"hi":>10}'  # 오른쪽 정렬
# '        hi'
# >>> f'{"hi":^10}'  # 가운데 정렬
# '    hi    '


# '%길이.자릿수f' % 숫자

# print('%10.2f' % 2.3)
# # '      2.30'
# print('%10.3f' % 2.3)
# # '     2.300'


# ->오른쪽 정렬
# >>> '%-10s' % 'python'
# 'python    '

#format 함수로 천단위 숫자 출력


# >>> format(1493500, ',')
# '1,493,500'

# import string
# sentences = input()
# sentences=sentences.strip(string.punctuation)
# sentences=sentences.strip(".,")
# sentences=sentences.replace(",","")
# sentences=sentences.split()

# # print(sentences)
# cnt =0
# for i,c in enumerate(sentences):
#     if c.strip(".,")=="the":
#         cnt+=1
# print(cnt)
# print(sentences.count("the"))
# print(sentences)
# for i,c in enumerate(sentences):
#     if c=="the":
#         if i!=0:
#             print(sentences[i-1])
#         print(i,c)
#         if i!=len(sentences)-1:
#             print(sentences[i+1])
# v=input().split(";")
# print(v)
values=list(map(int,input().split(";")))
values.sort(reverse=True)
for v in values:
    value = format(v,',')
    print(f"{value:>9}")
    
