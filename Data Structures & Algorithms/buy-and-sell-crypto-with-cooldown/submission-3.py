class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = {}
        
        def dfs(i, haveStock):

            if i >= n:
                return 0

            if (i, haveStock) in dp:        
                return dp[(i, haveStock)]

            curr = prices[i]
            if haveStock == True:
                ans = max(dfs(i + 1, True), curr + dfs(i + 2, False))

            else:
                ans = max(dfs(i + 1, False), -curr + dfs(i + 1, True))

            dp[(i, haveStock)] = ans
            return ans

        return dfs(0, False)