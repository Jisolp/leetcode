class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # fix one number 
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

        # two pointer on the suffix after that num 
            left = i + 1
            right = len(nums)-1

            while left < right and right < len(nums):
                currSum = nums[i] + nums[left] + nums[right]
                if currSum < 0:
                    left+= 1
                elif currSum > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return res