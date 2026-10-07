class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.n = len(nums)
        def back(i, subset):
            xorr = 0
            for num in subset:
                xorr ^= num
            self.res += xorr
            for j in range(i, self.n):
                subset.append(nums[j])
                back(j + 1, subset)
                subset.pop()
            
        back(0, [])
        return self.res