'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time
'''
class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        result = 0
        for n in hashset:
            if n-1 not in hashset:
                length = 1
                while n+length in hashset:
                    length += 1
                result = max(result, length)
        return result