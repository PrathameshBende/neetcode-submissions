class Solution:
    def isObs(self, i , j, grid):
        return 1 if grid[i][j] == 1 else 0

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        
        paths = [[0] * len(grid[0])] * len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    paths[0][0] = 1
                    continue
                if self.isObs(i, j, grid):
                    paths[i][j] = 0
                    continue
                if i == 0:
                    paths[i][j] = paths[i][j - 1]
                elif j == 0:
                    paths[i][j] = paths[i - 1][j]
                else:
                    paths[i][j] = paths[i][j - 1] + paths[i - 1][j]
        return paths[-1][-1]