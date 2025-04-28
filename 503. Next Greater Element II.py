from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]* len(nums)
        stack = []

        for i in range(2*len(nums)):
            real_idx = i % len(nums)
            while stack and nums[real_idx] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[real_idx]
            if i < len(nums):
                stack.append(real_idx)
        return res