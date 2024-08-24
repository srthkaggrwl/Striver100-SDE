class Solution(object):
    def majorityElement(self, nums):
        dict1 = {}

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        majority_element = []
        threshold = len(nums) // 3
        
        for key, value in dict1.items():
            if value > threshold:
                majority_element.append(key)
        
        return majority_element

solution = Solution()
print(solution.majorityElement([2, 3]))  
