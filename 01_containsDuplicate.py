'''
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
'''
nums = [1,2,3,4]
def containsDuplicates(nums):
    if len(nums) == len(set(nums)):
        return False
    return True

print(containsDuplicates(nums))

def containsDuplicates(nums):
    mp = {}
    for ele in nums:
        if ele in mp:
            return True
        mp[ele] = 1 + mp.get(ele, 0)
    return False

# hashset = set()
# for n in nums:
#     if n in hashset:
#         return True
#     hashset.add(n)
# return False
