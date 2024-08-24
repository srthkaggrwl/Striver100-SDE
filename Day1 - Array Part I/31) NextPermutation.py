class Solution(object):
    def nextPermutation(self, nums):

        break_point = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                break_point = i-1
                break
            
        if break_point == -1:
            nums.reverse()
            print(break_point)     
        else:
            for i in range(len(nums)-1, break_point, -1):
                if nums[i] > nums[break_point]:
                    second_greatest = i
                    break

            nums[second_greatest], nums[break_point] = nums[break_point], nums[second_greatest]
            nums[break_point+1:] = sorted(nums[break_point+1:])
            print(nums)
            print(break_point)

solution = Solution()
nums = [4,1,3,2]
solution.nextPermutation(nums)

