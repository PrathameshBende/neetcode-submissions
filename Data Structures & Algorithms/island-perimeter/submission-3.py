class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        first = (-1, -1)
        for i in range(n):
            to_break = False
            for j in range(m):
                if grid[i][j] == 1:
                    first = (i, j)
                    to_break = True
                    break
            if to_break == True:
                break
        if first == (-1, -1):
            return 0

        q = deque()
        q.append(first)
        visited = {first}
        ans = 0
        while(q):
            ans += 4
            i, j = q.popleft()

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    if grid[i + di][j + dj] == 1:
                        ans -= 1
                        if (i + di, j + dj) not in visited:
                            visited.add((i + di, j + dj))
                            q.append((i + di, j + dj))
            print(ans)

        return ans
