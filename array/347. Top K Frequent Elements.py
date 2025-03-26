from typing import List;

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort 
        ans = []
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for key, value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
     