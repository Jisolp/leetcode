from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(m+n)
        pointer1, pointer2 = 0, 0
        newArr = []

        while pointer1< len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                newArr.append(num1[pointer1])
                pointer1 += 1
            elif nums1[pointer1] > nums1[pointer2]:
                newArr.append(nums2[pointer2])
                pointer2 += 1
            else:#the same
                newArr.append(nums1[pointer1])
                pointer1+=1
            pointer2+=1
        while pointer1 < len(nums1):
            newArr.append(nums1[pointer1])
            pointer1 += 1
        while pointer2 < len(nums2):
            newArr.append(nums2[pointer2])
            pointer += 1
        
        n = len(newArr)
        if n % 2 == 1: 
            return newArr[n //2]
        else:
            return (newArr[n//2-1]+ newArr[n//2])/2

        # O(log(m+n))