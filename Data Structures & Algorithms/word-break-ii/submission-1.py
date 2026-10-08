class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        temp = []
        res = []
        n = len(s)
        def dfs(i, s):

            if i == n:
                s = ""
                for word in temp:
                    s = s + word + " "
                res.append(s[:-1])
                return 

            for j in range(i + 1, n + 1):
                if s[i : j] in wordDict:
                    temp.append(s[i:j])
                    dfs(j, s)
                    temp.pop()

        dfs(0, s)

        return res