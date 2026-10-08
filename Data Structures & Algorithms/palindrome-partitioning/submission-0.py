class Solution:
    def isPal(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def dfs(i, subset):
            if i == n:
                res.append(subset.copy())
                return
            for j in range(i + 1, n + 1):
                if self.isPal(s[i : j]):
                    subset.append(s[i : j])
                    dfs(j, subset)
                    subset.pop()
        dfs(0, [])
        return res