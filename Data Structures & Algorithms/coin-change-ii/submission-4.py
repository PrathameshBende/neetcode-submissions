class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * amount for _ in range(n)] 
        def dfs(idx, total):
            if total == amount:
                return 1
            if total > amount:
                return 0

            if dp[idx][total] != -1:
                return dp[idx][total]
            ans = 0
            for i in range(idx, n):
                ans += dfs(i, total + coins[i]) 
            dp[idx][total] = ans

            return dp[idx][total]

        return dfs(0, 0)