class Solution(object):
    def compareVersion(self, version1, version2):
        # Make a list of integers where each element is the map of integer value of char seperated by '.'
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))

        max_length = max(len(version1), len(version2))

        for i in range(max_length):
            # Get the current version number, defaulting to 0 if out of range
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0  

# Example usage:
solution = Solution()

# Test Case 1
version1 = "1.2"
version2 = "1.10"
print(solution.compareVersion(version1, version2))  # Output: -1

# Test Case 2
version1 = "1.0.1"
version2 = "1"
print(solution.compareVersion(version1, version2))  # Output: 1

# Test Case 3
version1 = "1.0"
version2 = "1.0.0"
print(solution.compareVersion(version1, version2))  # Output: 0
