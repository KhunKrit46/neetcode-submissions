class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1 
        middle = -1 
        while L <= R: 
            mid = ( L+R )// 2 
            if matrix[mid][0] <= target <= matrix[mid][-1]: 
                middle = mid
                break
            elif matrix[mid][0] > target: 
                R = mid - 1 
            else: 
                L = mid + 1 
        if middle == -1: 
            return False 

        L, R = 0, len(matrix[middle]) - 1 
        while L <= R: 
            mid = (L+R )// 2 
            if matrix[middle][mid] < target: 
                L = mid + 1 
            elif matrix[middle][mid] > target:
                R = mid - 1 
            else: 
                return True
        
        return False