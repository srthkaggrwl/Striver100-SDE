class Solution(object):
    def findDuplicate(self, nums):
        nums = sorted(nums)  

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == nums[i]:
                    return nums[i]
                elif nums[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

solution = Solution()
nums = [1, 3, 4, 4, 2]
print(solution.findDuplicate(nums))


'''
class Solution(object):
    def findDuplicate(self, nums):
        # Step 1: Initialize tortoise and hare
        tortoise = hare = nums[0]
        
        # Step 2: Finding the intersection point in the cycle
        while True:
            tortoise = nums[tortoise]  # move tortoise one step
            hare = nums[nums[hare]]    # move hare two steps
            if tortoise == hare:       # they meet, so there is a cycle
                break

        # Step 3: Finding the entrance to the cycle
        tortoise = nums[0]             # start tortoise at the beginning
        while tortoise != hare:        # move both one step at a time
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare  # or return tortoise, as they are equal now

# Example usage:
solution = Solution()
nums = [1, 3, 4, 2, 2]
print(solution.findDuplicate(nums))  # Output: 2

'''