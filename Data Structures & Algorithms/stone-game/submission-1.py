class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = {}
        def dfs(left, right, diff):
            if left > right:
                return diff > 0
            if (left, right) in dp:
                return dp[(left, right)]
            if (left + right) % 2 == 0:
                dp[(left, right)] = dfs(left + 1, right, diff + piles[left]) or dfs(left, right - 1, diff + piles[right])
                return dp[(left, right)]

            else:
                dp[(left, right)] = dfs(left + 1, right, diff - piles[left]) or dfs(left, right - 1, diff - piles[right])
                return dp[(left, right)]

        return dfs(0, n - 1, 0)