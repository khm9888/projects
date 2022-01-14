# # 6-2 문자열 뒤집기

# # 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라.
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, a_list: List[str]) -> None:
        # a_list.sort(reverse=True)
        a_list.reverse()
        # a_list[:]=a_list[::-1]
        return a_list