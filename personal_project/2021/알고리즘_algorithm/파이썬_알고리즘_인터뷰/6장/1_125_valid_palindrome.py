# # 6-1 유효한 팰린드롬

# # 주어진 문자열이 팰린드롬인지 확인하라. 대소무자를 구분하지 않으며, 영문자와 숫자 만을 대상으로 한다. 
# https://leetcode.com/problems/valid-palindrome/

# class Solution:
    # def isPalindrome(self,text):
    #     text_reverse = text[::-1]
    #     text = text.lower()
    #     text_reverse = text_reverse.lower()
    #     t1 = ""
    #     t2 = ""
    #     for x in text:
    #         if x.isalnum():
    #             t1+=x
    #     for x in text_reverse:
    #         if x.isalnum():
    #             t2+=x
    #     if t1==t2:
    #         return True
    #     return False

# v=palindrom("A man, a plan, a canal: Panama")
# print(v)          

class Solution:
    def isPalindrome(self,text):
        text = text.lower()
        # 정규식으로 불필요한 문자 필터링
        text = re.sub('[^a-z0-9]','',text)

        return text == text[::-1]
