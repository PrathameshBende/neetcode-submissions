class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False]*n
        def dfs(i, subset, visited):
            
            if i == n:
                res.append(subset.copy())
                return 

            for j in range(n):
                if visited[j]:
                    continue
                subset.append(nums[j])
                visited[j] = True
                dfs(i +  1, subset, visited)
                subset.pop()
                visited[j] = False
                
        dfs(0, [], visited)

        return res
