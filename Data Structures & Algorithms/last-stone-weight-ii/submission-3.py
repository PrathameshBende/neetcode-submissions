class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        n = len(stones)
        target = s // 2

        dp = [[-1] * (target + 1) for _ in range(n)]

        def dfs(i, wt):
            if i == n:
                return abs(s - 2 * wt)

            if dp[i][wt] != -1:
                return dp[i][wt]

            ans = dfs(i + 1, wt)

            if wt + stones[i] <= target:
                ans = min(ans, dfs(i + 1, wt + stones[i]))

            dp[i][wt] = ans
            return ans

        return dfs(0, 0)