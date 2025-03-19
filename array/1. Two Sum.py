from typing import List;

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compSet = {}

        for index, num in enumerate(nums):
            comp = target - num
            if comp in compSet:
                return [index,compSet[comp]]
            compSet[num] = index 
        return None