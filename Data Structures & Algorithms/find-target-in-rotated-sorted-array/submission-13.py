class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            print(nums[left], nums[mid], nums[right], target)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid] and nums[mid] < target:
                left = mid + 1
            elif nums[left] < target and target < nums[mid]:
                right = mid - 1
            
            elif nums[mid] < target and target < nums[left]:
                left = mid + 1
            elif target < nums[mid] and nums[mid] < nums[left]:
                right = mid - 1

            elif target < nums[left] and nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] == target else -1