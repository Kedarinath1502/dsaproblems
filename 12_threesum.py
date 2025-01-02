'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i == 0 and a > 0:
                break
            if i>0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right and i < len(nums) -2:
                currsum = a + nums[left] + nums[right]
                if currsum < 0:
                    left += 1
                elif currsum > 0:
                    right -= 1
                else: 
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left< right:
                        left += 1
        return res