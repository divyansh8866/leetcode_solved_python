"""
By: Divyansh Patel

QUESTION
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

# SOULTION 
# solved using consecept of slicing the list. This method is inefficient for large list and large numbers. Go to second method.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i==len(nums):
                if sum(nums[:i])==0 :
                    return i 
                else :
                    continue
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1

# SOLUTION
# sloved using the summing and dividing equaly.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        targeted_sum = 0
        for i,v in enumerate(nums):
            targeted_sum = (total_sum -v)/2
            # print(f"right sum should be {i} : {targeted_sum} ")
            if (targeted_sum-int(targeted_sum))==0:
                if sum(nums[:i])==targeted_sum:
                    # print(f"Is Piviot index {i}")
                    return i
                else :
                    continue
        return -1
               