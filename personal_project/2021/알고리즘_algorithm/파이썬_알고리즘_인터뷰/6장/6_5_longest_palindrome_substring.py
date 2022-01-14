# # 6_5_longest_palindrome_substring

# # 가장 긴 팰린드롬 부분 문자열을 출력하라.
# https://leetcode.com/problems/longest-palindromic-substring/

# #1. 시간초과 코드

# class Solution:
#     def longestPalindrome(self,text):
#         result = list()
#         leng = len(text)
#         for i in range(leng):#0~4
#             for j in range(i+1,leng+1):#1~5
#                 test_word = text[i:j]
#                 # print(i,j,test_word)
#                 # if len(test_word)
#                 if test_word == test_word[::-1]:
#                     result.append(test_word)
#         result.sort(key = lambda x:len(x),reverse=True)
#         return result[0]
# c= Solution()      

# text = "babad"
# print(c.longestPalindrome(text))


#2. 책에서 만들어준 코드 - 풀이 다시 볼 것
class Solution:
    def longestPalindrome(self,s):
        def expand(left,right):
            while left>=0 and right<=len(s) and s[left]==s[right-1]:
                left -=1
                right +=1
            return s[left+1:right-1]
        
        #1글자거나, 전체가 펠린드롬이면 그냥 패스
        if len(s)<2 or s==s[::-1]:
            return s
        result = ""
        for i in range(len(s)-1):
            result = max(result,expand(i,i+1),expand(i,i+2),key=len)
        return result
    

c= Solution()
print(c.longestPalindrome("asdffds"))
