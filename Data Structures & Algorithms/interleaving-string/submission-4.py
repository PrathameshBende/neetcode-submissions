class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" and s2 == "" and s3 == "":
            return True
        if s2 == "" and s1 != s3:
            return False
        if s1 == "" and s2 != s3:
            return False
        dp = [[-1] * (1 + len(s2)) for _ in range(len(s1) + 1)]

        def dfs(i, j, curr, ans):
            if i + j == len(s3) - 1:
                return True

            if dp[i][j] == 0 or dp[i][j] == 1:
                return dp[i][j]

            ans1 = ans2 = False
            if i < len(s1) and s1[i] == s3[i + j]:
                ans1 = dfs(i + 1, j, curr + s1[i], False)

            if j < len(s2) and s2[j] == s3[i + j]:
                ans2 = dfs(i, j + 1, curr + s2[j], False)
            dp[i][j] = 0 if (ans1 or ans2) == False else 1
            return dp[i][j]

        return True if dfs(0, 0, "", False) == 1 else False