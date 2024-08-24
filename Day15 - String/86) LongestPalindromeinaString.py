class Solution(object):
    def longestPalindrome(self, s):
        n = len(s) 
    
        L = [[0 for x in range(n)] for x in range(n)]
        print(L)

        for i in range(n): 
            L[i][i] = 1

        print(L)    
solution = Solution()
solution.longestPalindrome("abcabcba")



