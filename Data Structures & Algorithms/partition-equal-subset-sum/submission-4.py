class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target = target // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, - 1, - 1):
            nextdp = set()
            for s in dp:    
                if nums[i] + s == target:
                    return True
                nextdp.add(s)
                nextdp.add(nums[i] + s)
            dp = nextdp
        return False