# # 6-4 가장 흔한 단어

# # 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등 또한 무시한다.)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = "a, a, a, a, b,b,b,c, c"
banned=["a"]
from collections import Counter

class Solution:
    # def __init__(self):
    #     pass
    def mostCommonWord(self,text,banned=None):
        
        text = text.strip()
        text_filter=str()
        for t in text: 
            if t.isalpha() or t==" ":
                text_filter+=t
            else:
                text_filter+=" "

        text_filter=text_filter.lower()
        # print(text_filter)
        count_list = text_filter.split()
        print(26,banned)
        # print(count_list)
        if banned:
            for b in banned:
                while b in count_list:
                    count_list.remove(b)
        print(count_list)
        count_text = Counter(count_list)
        # print(count_text)
        # print(count_text.most_common(1))
        # print(count_text.most_common(1)[0])
        # print(count_text.most_common(1)[0][0])
        return count_text.most_common(1)[0][0]
        
c= Solution()      

print(c.mostCommonWord(paragraph,banned))
# #책 통해서 다시 코드 구현
 
# import re
# from collections import Counter

# def most_common_word(paragraph:str, banned: list) ->str:
#     words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    
#     counts = Counter(words)
#     print(counts)
#     return counts.most_common(1)[0][0]

# v=most_common_word(paragraph,[])

# print(v)