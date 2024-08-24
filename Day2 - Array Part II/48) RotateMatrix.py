class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)        
        
        i=0
        j=len(matrix[0]) - 1
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
            #print(matrix[i])

        print(matrix)        



solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)