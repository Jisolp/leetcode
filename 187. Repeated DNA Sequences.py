class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaSet = set()
        ans = set()

        for left in range(len(s)-9):
            if s[left:left+10] in dnaSet:
                ans.add(s[left:left+10])
            dnaSet.add(s[left:left+10])
        return list(ans)
