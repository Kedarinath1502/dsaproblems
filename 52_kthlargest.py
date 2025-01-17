'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-num for num in nums]
        heapq.heapify(minheap)
        while k > 0:
            res = heapq.heappop(minheap)
            k -= 1
        return res*-1