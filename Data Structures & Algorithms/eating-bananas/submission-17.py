class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            total = sum((pile + mid - 1) // mid for pile in piles)
            
            if total <= h:
                right = mid
            else:
                left = mid + 1
        
        return left

        # maxi = max(piles)
        # mini = 1
        # low = mini
        # high = maxi 
        
        # while low <= high:
        #     count = 0
        #     mid = low + (high - low)//2

        #     for i in range(len(piles)):
        #         count += (piles[i] + mid - 1) // mid

        #     if count > h:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        #     print(low, count, mid)
        # if low > maxi:
        #     return maxi
        # return low