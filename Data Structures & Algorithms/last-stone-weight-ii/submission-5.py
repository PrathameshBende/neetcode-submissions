class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for w in range(target, stone - 1, -1):
                if dp[w - stone]:
                    dp[w] = True

        for w in range(target, -1, -1):
            if dp[w]:
                return s - 2 * w