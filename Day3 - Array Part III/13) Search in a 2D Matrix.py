class Solution(object):
    def searchMatrix(self, matrix, target):
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        
        return False
    
solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(solution.searchMatrix(matrix, 3)    )


