'''
Q3. TWO SUM : Given an array of integer numbers and an integer target, return indices of the two numbers such that they add up to target.

	Create a hashmap and iterate over the array and add the element into the hashmap by checking whether target - current element is already stored in hashmap.
'''

def twoSum(arr, target):
    hashmap = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hashmap[i]:
            return [hashmap[complement], i]
        hashmap[arr[i]] = i
