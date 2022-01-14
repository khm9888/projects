## 질문

# 팔린드롬( 앞뒤가 똑같은 문자 확인하는 함수 만들기 ex.) 리효리)) 문제

# 답은 True, False 인데... 이렇게 하면 둘다 False로 나오네요.. ㅠ 어디가 틀렸을까요?

import re

def palindrome(str):
    str.lower()
    s = re.sub(r'[^\w]', '', str).lower()

    return s == s[::-1]

print(palindrome('A man, a plan, a canal: Panama'))
print(palindrome("race a car"))
