class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        low = 1
        high = x//2
        target = x
        while low <= high:
            mid = low + (high - low)//2
            if mid*mid == target:
                return mid
            elif mid*mid < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low - 1