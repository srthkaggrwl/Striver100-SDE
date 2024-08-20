class Solution(object):
    def longestConsecutive(self, nums):
        
        num_set = set(nums)    #O(n)
        print(num_set)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(current_streak, longest_streak)


        print(longest_streak)        
                     

solution = Solution()
#solution.longestConsecutive([100,4,200,1,3,2])        
solution.longestConsecutive([0,3,7,2,5,8,4,6,0])