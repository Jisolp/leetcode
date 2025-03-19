from typing import List;

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,left,mid,right):
            leftArr = arr[left:mid+1]
            rightArr = arr[mid+1:right+1]
            l,r,i= 0,0,left
            while l < len(leftArr) and r < len(rightArr):
                if leftArr[l] < rightArr[r]:
                    arr[i] = leftArr[l]
                    l += 1
                else:
                    arr[i] = rightArr[r]
                    r+= 1
                i += 1

            while l < len(leftArr):
                arr[i] = leftArr[l]
                l += 1
                i += 1
            while r < len(rightArr):
                arr[i] = rightArr[r]
                r += 1
                i += 1
       #def merge(arr, left, middle, right)
       # set the pointers 
       # point to arr
       # while the pointers are not out of bounds
       # replace the value with whichever value is small
       # if the pointers are out of bounds, enter a while loop to input the rest of the arr

        # def mergesort(arr, left, right)
        def mergeSort(arr, left, right):
            if left == right:
                return arr
            mid = (left+right)//2
            mergeSort(arr,left,mid)
            mergeSort(arr,mid+1,right)
            merge(arr,left,mid,right)
            return arr
        # divide it in the middle 
        # recurisvely call on mergesort 
        # call merge of the (arr, left, middle, right)
        return mergeSort(nums,0, len(nums)-1)
