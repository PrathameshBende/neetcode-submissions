class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        ans = 0
        for new_i in range(n):
            for new_j in range(m):
                if grid[new_i][new_j] == "1":
                    if not visited[new_i][new_j]:
                        
                        ans += 1
                        q = deque()
                        q.append((new_i, new_j))
                        visited[new_i][new_j] = True
                        while q:
                            i, j = q.popleft()
                            for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                                ni = i + di
                                nj = j + dj
                                if 0 <= ni < n and 0 <= nj < m:
                                    if grid[ni][nj] == "1":
                                        if not visited[ni][nj]:
                                            q.append((ni, nj))
                                            visited[ni][nj] = True  
        
        return ans