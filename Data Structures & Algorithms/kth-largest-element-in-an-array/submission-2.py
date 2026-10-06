class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.nlargest(k, nums, key=None)
        return heap[-1]