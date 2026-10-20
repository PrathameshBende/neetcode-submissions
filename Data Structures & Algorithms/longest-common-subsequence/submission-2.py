class Solution:
    def dfs(self, i, j, t1, t2):
        if i == self.n1 or j == self.n2:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        if t1[i] == t2[j]:
            self.dp[i][j] = 1 + self.dfs(i + 1, j + 1, t1, t2)
        
        else:
            self.dp[i][j] = max(
                self.dfs(i + 1, j, t1, t2),
                self.dfs(i, j + 1, t1, t2)
            )

        return self.dp[i][j]

    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        self.n1 = len(t1)
        self.n2 = len(t2)
        n = max(self.n1, self.n2)
        self.dp =  [[-1] * self.n2 for _ in range(self.n1)]
        return self.dfs(0, 0, t1, t2)