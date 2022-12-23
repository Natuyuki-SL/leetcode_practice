'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
def twoSum(nums, target):
        pos1 = 0
        pos2 = 1
        while (nums[pos1] + nums[pos2]) != target:
            if pos2 < len(nums)-1:
                pos2 +=1
            elif pos2 - pos1 > 1:
                pos1 +=1
                pos2 = pos1 + 1
        return [pos1, pos2]

nums = [2,7,11,15]
print(twoSum(nums, 9))