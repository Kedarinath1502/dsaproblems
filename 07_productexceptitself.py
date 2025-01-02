'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        res = [1] * len(nums)
        left_prod = 1
        for i in range(len(nums)):
            res[i] = left_prod
            left_prod = left_prod * nums[i]
        right_prod = 1
        for i in range(len(nums)-1,-1,-1): 
            res[i] = res[i]*right_prod
            right_prod = right_prod * nums[i]
        return res
'''

class Solution(object):
    def productExceptSelf(self, nums):
        zero_count = nums.count(0)
        if zero_count >1:
            return [0]* len(nums)
        if zero_count==1:
            product = 1
            for i in nums:
                if i!=0:
                    product = product*i
            return [product if i==0 else 0 for i in nums]
        product =1
        for num in nums:
            product = product * num
        return [product//num for num in nums]