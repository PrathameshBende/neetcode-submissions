class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        res = []
        for i in range(1, n + 1):
            nums.append(i)

        def dfs(i, subset):

            if len(subset) == k:
                res.append(subset.copy())
                return

            elif i == n and len(subset) == k:
                res.append(subset.copy())
                return

            elif i == n and len(subset) != k:
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])

        return res