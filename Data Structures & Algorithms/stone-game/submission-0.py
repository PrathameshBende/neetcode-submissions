class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        def dfs(left, right, diff):
            if left > right:
                return diff > 0

            if (left + right) % 2 == 0:
                ans = dfs(left + 1, right, diff + piles[left]) or dfs(left, right - 1, diff + piles[right])
                return ans

            else:
                ans = dfs(left + 1, right, diff - piles[left]) or dfs(left, right - 1, diff - piles[right])
                return ans

        return dfs(0, n - 1, 0)