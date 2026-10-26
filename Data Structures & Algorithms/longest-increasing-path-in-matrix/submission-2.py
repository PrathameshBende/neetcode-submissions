class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        def dfs(row, col):

            if dp[row][col] != -1:
                return dp[row][col]
            meetha = 1
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= row + i < n and 0 <= col + j < m:
                    if matrix[row + i][col + j] > matrix[row][col]:
                        meetha = max(meetha, 1 + dfs(row + i, col + j))
            dp[row][col] = meetha
            return dp[row][col]
        ans = -1
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans