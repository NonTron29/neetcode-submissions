class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])


        row = -1
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                row = i
                break
        
        if row == -1:
            return False 

        low = 0
        high = n - 1

        while(low <= high):
            mid = low + (high - low) // 2
            if(matrix[row][mid] == target):
                return True
            if(matrix[row][mid] < target):
                low = mid + 1
            if(matrix[row][mid] > target):
                high = mid - 1         
        
        return False 