from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # count = defaultdict(int)

        # for n in nums:
        #     count[n] += 1
        #     if len(count) <= 2:
        #         continue 
        #     newCount = defaultdict(int)
        #     for i,c in enumerate(count):
        #         if c > 1:
        #             newCount[n] = c-1
        #     count = newCount
        # ans = []
        # for n in count:
        #     if nums.count(n) > len(count)//3:
        #         ans.append(n)
        # return ans
        count1 , count2 = 0,0
        can1, can2 = None, None

        for n in nums: 
            if n == can1:
                count1 += 1
            elif n == can2:
                count2 += 1
            elif count1 == 0:
                can1 = n
                count1 = 1
            elif count2 == 0 :
                can2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        for c in (can1, can2):
            if nums.count(c) > len(nums)//3:
                ans.append(c)
        return ans