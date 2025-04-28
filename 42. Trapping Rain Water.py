from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left,right = 0, len(height) -1
        maxLeft, maxRight = height[left], height[right]
        water = 0 

        while left < right and right < len(height):
            if maxLeft < maxRight:
                #increment left pointer
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]

            else:
                #decrement right pointer
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
        return water