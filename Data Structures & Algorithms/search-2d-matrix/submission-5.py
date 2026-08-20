class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(mat[0]) - 1
        top = 0
        bottom = len(mat) - 1
        while(top <= bottom):
            mid = top + (bottom - top)//2
            
            if mat[mid][0] == target:
                return True
            elif mat[mid][0] < target:
                top = mid + 1
            else: 
                bottom = mid - 1

        while left <= right:
            mid = left + (right - left)//2
            
            if mat[bottom][mid] == target:
                return True
            elif mat[bottom][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False