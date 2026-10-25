class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, total):
            if i == n:
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            ans = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            dp[(i, total)] = ans
            return ans

        return dfs(0, 0)