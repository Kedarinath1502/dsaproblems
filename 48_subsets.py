'''Given an integer array nums of unique elements, return all possible subsets (power set)
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                print(res)
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subset = []
            for subset in res:
                new_subset.append(subset + [num])
            res += new_subset
        return res