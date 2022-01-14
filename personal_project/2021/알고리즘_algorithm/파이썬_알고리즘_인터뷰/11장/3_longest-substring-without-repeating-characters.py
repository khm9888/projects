# # 11-3 중복 문자 없는 가장 긴 부분 문자열

# # 중복 문자가 없는 가장 긴 부분 문자열_substring_의 길이를 리턴하라
# # https://leetcode.com/problems/longest-substring-without-repeating-characters/
# # 파일 이름 고치기


# from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used={}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 "start" 위치 갱신
            # print(f"char: {char}")
            if char in used and start <= used[char]:
                start = used[char] + 1
                # print(True)
            else: #최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
                # print(False)
                
            # print(f"max_length: {max_length}")
            # 현재 문자의 위치 삽입
            used[char] = index
            
        return max_length        
c= Solution()
print(c.lengthOfLongestSubstring("abcabcbb"))
