from typing import List 

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
        # subarry = 0 
        # left = 0
        # right = left + 1
        # while left < right and left < len(nums):
        #     if nums[left] == k:
        #         subarry += 1
        #         left = right
        #         right = left + 1
        #     elif nums[left] < k:
        #        sumNums =  nums[left] + nums[right]
        #        while sumNums < k:
        #             right += 1
        #             sumNums += nums[right]
        #         if sumNums == k:
        #             subarry += 1
        #             left = right 
        #             right += 1
        #         else:
        #             left +=1 
        #             right = left + 1
        #     elif nums[left] > k:
        #         left = right
        #         right = left + 1 
            
        # return subarry
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0 
        count = 0
        prefixMap = {0:1}

        for num in nums:
            prefix += num
            if prefix - k in prefixMap:
                count += prefixMap[prefix-k]
            prefixMap[prefix] = prefixMap.get(prefix,0)+1
        return count 