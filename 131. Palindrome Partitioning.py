from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return 
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res

    def isPalindrome(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True