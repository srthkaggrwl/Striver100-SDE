class Solution(object):
    def majorityElement(self, nums):
        dict1 = {}

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        majority_element = max(dict1, key=dict1.get)
        
        print(majority_element)

solution = Solution()
solution.majorityElement([3, 3, 4])  