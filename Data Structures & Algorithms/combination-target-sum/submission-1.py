class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        tmp = set()
        def dfs(i, sum, subset):
            if sum > target:
                return
            
            elif sum == target:
                tmp.add(tuple(sorted(subset)))
                return
            
            else:
                for j in range(i, n):
                    sum += nums[j]
                    subset.append(nums[j])
                    dfs(j, sum, subset)
                    sum -= nums[j]
                    subset.pop()
        dfs(0, 0, [])
        res = [list(x) for x in tmp]
            
        return res