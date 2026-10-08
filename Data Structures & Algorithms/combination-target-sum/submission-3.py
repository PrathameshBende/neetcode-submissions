class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dfs(i, sum, subset):
            
            if sum == target:
                res.append(subset.copy())
                return
            
            else:
                for j in range(i, n):
                    if sum + nums[j] > target:
                        break

                    sum += nums[j]
                    subset.append(nums[j])
                    dfs(j, sum, subset)
                    sum -= nums[j]
                    subset.pop()

        dfs(0, 0, [])
            
        return res