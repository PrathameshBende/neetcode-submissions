class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        temp = []
        res = []
        n = len(s)
        wordDict = set(wordDict)
        def dfs(i, s):

            if i == n:
                res.append(" ".join(temp))
                return 

            for j in range(i + 1, n + 1):
                if s[i : j] in wordDict:
                    temp.append(s[i:j])
                    dfs(j, s)
                    temp.pop()

        dfs(0, s)

        return res