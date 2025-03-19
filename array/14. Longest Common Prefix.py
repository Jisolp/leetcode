from typing import List;

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize answer string 
        ans = ""
        # sort out the strs in the the list 
        sortedStrs = sorted(strs)
        # compare the first and last word in the sorted 
        first, last = sortedStrs[0], sortedStrs[-1]
        # if the letters are equal then add it to ans
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                return ans
        return ans
        # other wise stop and return ans 
