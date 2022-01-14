# # 12-2 전화 번호 문자 조합

# # 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
# # https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# # 파일 이름 고치기



#1번 내가 짠 코드
""" 
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_alpha_dict = {}
        num_to_alpha_dict["2"]=list("abc")
        num_to_alpha_dict["3"]=list("edf")
        num_to_alpha_dict["4"]=list("ghi")
        num_to_alpha_dict["5"]=list("jkl")
        num_to_alpha_dict["6"]=list("mno")
        num_to_alpha_dict["7"]=list("pqrs")
        num_to_alpha_dict["8"]=list("tuv")
        num_to_alpha_dict["9"]=list("wxyz")
        result = list()
        for n in digits:
            alphas = num_to_alpha_dict[n]
            if not result:
                result = num_to_alpha_dict[n]
                continue
            c_result = result.copy()
            result = list()
            for c in c_result:
                for a in alphas:
                   result.append(c+a)
        return result
            
    
c= Solution()
print(c.letterCombinations("23"))

 """
#2번 모든 경우를 한다는 경우

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #digit은 숫자 ex>"23"
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path)==len(digits):
                result.append(path)
                return
            
            #입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)
                    
        # 예외처리
        if not digits:
            return []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        result = []
        dfs(0,"")
        
        return result
    
c= Solution()
print(c.letterCombinations("23"))
