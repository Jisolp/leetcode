from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len(s1)>len(s2)
        s1Count = Counter(s1)
        s2Window = Counter(s2[:len(s1)])

        if s1Count == s2Window:
            return True

        for i in range(len(s1),len(s2)):
            s2Window[s2[i]] += 1
            s2Window[s2[i-len(s1)]] -= 1
            
            if s2Window[s2[i-len(s1)]] == 0:
                del s2Window[s2[i-len(s1)]]
            if s1Count == s2Window:
                return True
        return False