import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        n = len(nums)
        self.pq = nums
        heapq.heapify(self.pq)
        self.k1 = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        while(len(self.pq) > self.k1):
            heapq.heappop(self.pq)
        return self.pq[0]