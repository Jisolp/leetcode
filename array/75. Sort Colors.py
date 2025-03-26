from typing import List;

class Solution:
    def sortColors(self, nums: List[int]) -> None: 
        count = [0]*3
        
        for i in nums:
            count[i] += 1
       
        R, W, B = count
        nums[0:R] = [0]*R
        nums[R:R+W] = [1]*W
        
        nums[R+W:] = [2]*B
        return nums

        