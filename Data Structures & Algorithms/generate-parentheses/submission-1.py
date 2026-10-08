class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = "("
        def dfs(opened, closed, i, s):
            if i == n*2:
                res.append(s)
                return
            elif opened == closed:
                s += "("
                opened += 1
                dfs(opened, closed, i + 1, s)
                s = s[:-1]
                opened -= 1

            else:
                if opened < n:
                    s += "("
                    opened += 1 
                    dfs(opened, closed, i + 1, s)
                    s = s[:-1]
                    opened -= 1

                s += ")"
                closed += 1
                dfs(opened, closed, i + 1, s)
                s = s[:-1]
                closed -= 1    

        dfs(1, 0, 1, s)

        return res