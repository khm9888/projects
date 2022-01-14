# # 6-5 그룹 애너그램

# # 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# https://leetcode.com/problems/group-anagrams/

import collections

class Solution:
    def groupAnagrams(self, strs):
        # check_dict = dict()
        check_dict = collections.defaultdict(list)
        for w in strs:
            check_dict["".join(sorted(w))].append(w)
                
        return list(check_dict.values())                 
            
c= Solution()      
strs = ["eat","tea","tan","ate","nat","bat"]
print(c.groupAnagrams(strs))

