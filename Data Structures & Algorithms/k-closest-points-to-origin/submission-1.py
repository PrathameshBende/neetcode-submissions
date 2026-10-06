class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:            
            heapq.heappush(heap, [(point[0] * point[0] + point[1] * point[1])**0.5, point])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans