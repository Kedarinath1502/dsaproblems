''' 
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        freq = [[] for _ in range(len(nums)+1)]
        for ele in nums:
            hashmap[ele] = 1 + hashmap.get(ele, 0)
        for key, value in hashmap.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                res += freq[i]
            if len(res) >= k:
                return res[0:k]