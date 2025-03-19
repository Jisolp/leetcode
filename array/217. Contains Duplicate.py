from typing import List;

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a hashset
        numSet = set()
        #iterate through the nums
        for i in nums:
            #if it is not in the set add it to the set
            if i not in numSet:
                numSet.add(i)
            #if already exists then return false 
            else:
                return True
        #return true
        return False
