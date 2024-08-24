class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        sum_ = [nums[i],nums[j],nums[k],nums[l]]
                        if nums[i]+nums[j]+nums[k]+nums[l] == target and sum_ not in ans:
                            ans.append([nums[i],nums[j],nums[k],nums[l]])
        
        unique = set(tuple(sorted(sublist)) for sublist in ans)
        return [list(tup) for tup in unique]
        

solution = Solution()
print(solution.fourSum([-5,5,4,-3,0,0,4,-2], 4)) #Output = [[2,2,2,2,2]]