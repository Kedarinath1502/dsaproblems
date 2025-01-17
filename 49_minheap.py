'''
implement the KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the 
stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element 
representing the kth largest element in the pool of test scores so far.'''

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
    