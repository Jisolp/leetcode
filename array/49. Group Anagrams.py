from typing import List;
from collections import defaultdict;

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each of the words in the list 
        ans = defaultdict(list)
        for word in strs: 
            count = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
            ans[tuple(count)].append(word)
        return list(ans.values())
