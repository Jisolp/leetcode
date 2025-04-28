class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxLength = 0
        res = ""

        #odd case 
        for i in range(len(s)):
            left , right = i , i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left + 1) > maxLength:
                    maxLength = right-left + 1
                    res = s[left:right+1]
                left-=1
                right+=1

        #even case
            left , right = i , i +1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left + 1) > maxLength:
                    maxLength = right-left + 1
                    res = s[left:right+1]
                left-=1
                right+=1
        return res