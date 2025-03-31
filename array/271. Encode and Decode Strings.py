from typing import List;

class Solution:
    def encode(self, strs: List[str]) -> str: 
        ans = ""
        for word in strs:
            ans += str(len(word))+"#"+word
        return ans
    def decode(self, s: str) -> List[str]:
        # when encountering a len of the word and # separate the words 
        ans = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+length+1]
            i = j+length+1
            ans.append(word)
            j = i 
        return ans 
            