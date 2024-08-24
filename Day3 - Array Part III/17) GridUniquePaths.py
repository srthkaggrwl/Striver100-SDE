import math

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        paths = math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))

        return int(paths)
    
solution = Solution()
print(solution.uniquePaths(3,7)    )