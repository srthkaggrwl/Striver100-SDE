# Space Complexity O(m+n)
'''
class Solution(object):
    def setZeroes(self, matrix):
        columns = [1]*len(matrix[0])
        rows = [1]*len(matrix)
        for i in range(len(rows)):
            for j in range(len(columns)):
                if matrix[i][j] == 0:
                    columns[j] = 0
                    rows[i] = 0
        print(columns)
        print(rows)            
        
        for i in range(len(rows)):
            for j in range(len(columns)):
                if rows[i] == 0:
                    matrix[i][j] = 0

        for i in range(len(columns)):
            for j in range(len(rows)):
                if columns[i] == 0:
                    matrix[j][i] = 0               


        print(matrix)    
                    

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
solution.setZeroes(matrix)                    '''



class Solution(object):
    def setZeroes(self, matrix):
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        print(matrix)
                    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

solution = Solution()
solution.setZeroes(matrix)                    