class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        mini = 1
        low = mini
        high = maxi 
        
        while low <= high:
            count = 0
            mid = low + (high - low)//2

            for i in range(len(piles)):
                count += (piles[i] + mid - 1) // mid

            if count > h:
                low = mid + 1
            else:
                high = mid - 1
            print(low, count, mid)
        if low > maxi:
            return maxi
        return low