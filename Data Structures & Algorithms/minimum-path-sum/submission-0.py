class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m] * n

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]

                else:
                    dp[i][j] = min(dp[i - 1][j] , dp[i][j - 1]) + grid[i][j]

        
        return dp[-1][-1]