'''
Given an array, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != k:
            k_start = len(nums)-k #where the nums need to be shifted to start
            if k == len(nums):
                pos_to_start = k
                start = 0
                while k_start < len(nums):
                    nums[start], nums[pos_to_start] = nums[k_start], nums[start]
                    k_start +=1
                    start +=1
                    pos_to_start +=1
                while pos_to_start < len(nums):
                    nums[pos_to_start] = nums[start]
                    pos_to_start +=1
            elif k > len(nums):
                k = k%len(nums)
                k_start = len(nums)-k
                nums[:] = nums[k_start:] + nums[:k_start]
            else:
                nums[:] = nums[k_start:] + nums[:k_start]





