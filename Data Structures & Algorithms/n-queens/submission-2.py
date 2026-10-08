class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        left_d = [True] * (2*n - 1)
        right_d = [True] * (2*n - 1)   
        col_d = [True] * n

        def place(row, col):
            left_d[row + col] = False
            right_d[row - col + n - 1] = False
            col_d[col] = False

        def unplace(row, col):
            left_d[row + col] = True
            right_d[row - col + n - 1] = True
            col_d[col] = True
        
        def Qstring(col):
            return "." * col + "Q" + "." * (n - col - 1)
        temp = []
        res = []
        def dfs(row):
            if row == n:
                res.append(temp.copy())
                return
            for col in range(n):
                if left_d[row + col] and right_d[row - col + n - 1] and col_d[col]:
                    place(row, col)
                    temp.append(Qstring(col))
                    dfs(row + 1)
                    temp.pop()
                    unplace(row, col)
    
        dfs(0)
        print(res) 

        return res   