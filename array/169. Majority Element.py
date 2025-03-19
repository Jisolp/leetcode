from typing import List;

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # #hash table 
        # # highest value retunr the key 
        # numTable = {}
        # for i in nums: 
        #     if i not in numTable:
        #         numTable[i] = 0
        #     numTable[i] += 1
        # return max(numTable,key = numTable.get)
        count = 0 
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -=1
        return candidate