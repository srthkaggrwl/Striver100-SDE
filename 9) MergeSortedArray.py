class Solution(object):
    def merge(self, nums1, m, nums2, n):      

        # Start filling nums1 from the end
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        # If nums2 is not fully traversed, fill nums1 with remaining elements of nums2
        if n > 0:
            nums1[:n] = nums2[:n]



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  
