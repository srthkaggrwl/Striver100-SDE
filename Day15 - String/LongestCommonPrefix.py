class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Start with the first string in the array as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the array
        for string in strs[1:]:
            # Trim the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage:
solution = Solution()

# Test Case 1
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

# Test Case 2
strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""
