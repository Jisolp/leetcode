class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of s and t are the same
        if len(s) != len(t):
            return False
        # hashtable for s
        sSet = {}
        for i in range(len(s)):
            if s[i] not in sSet:
                sSet[s[i]] = 1
            else:
                sSet[s[i]] +=1

        # hashtable for t
        tSet = {}
        for i in range(len(t)):
            if t[i] not in tSet:
                tSet[t[i]] = 1
            else:
                tSet[t[i]] += 1
        return sSet == tSet        
