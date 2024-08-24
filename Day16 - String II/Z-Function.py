class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack or not needle:
            return
        
        len_of_haystack = len(haystack)
        len_of_needle = len(needle)

        for i in range(0,len_of_haystack):
            temp = haystack[i:i+len_of_needle]
            if temp == needle:
                print(i, temp)
                break
            #print(temp)

        print(-1)


solution = Solution()
haystack = "leetcode"
needle = "leeto"
solution.strStr(haystack, needle)
        