'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        curSum = 0
        while left <= right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return [left+1, right+1]
            elif curSum < target:
                left = left + 1
            else:
                right = right -1
        return []