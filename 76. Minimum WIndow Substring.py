from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""
        
        tCount = Counter(t)
        sWindow = {}

        minLength = float('infinity')
        minRange = [-1,-1]
        left = 0 
        have, need = 0, len(tCount)

        for right in range(len(s)):
            sWindow[s[right]] = sWindow.get(s[right],0) + 1

            if s[right] in tCount and sWindow[s[right]] == tCount[s[right]]:
                have += 1
            
            while have == need:
                # decrease my left pointer
                if (right - left + 1) < minLength:
                    minLength = right-left+1
                    minRange = [left, right]

                sWindow[s[left]] -= 1
                if s[left] in tCount and sWindow[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
        left, right = minRange
        return s[left: right +1 ] if minLength != float('infinity') else ""