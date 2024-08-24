class Solution(object):
    def lengthOfLongestSubstring(self, s):
        print(set(s))
        # Initialize pointers and a set to track characters in the current window
        left = 0
        char_set = set()
        max_length = 0

        # Iterate over the string with the 'right' pointer
        for right in range(len(s)):
            # If the character is already in the set, move 'left' to the right until the character can be removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                print(char_set)

            # Add the current character to the set
            char_set.add(s[right])
            print(char_set)
            # Update the max_length with the size of the current window
            max_length = max(max_length, right - left + 1)

        print(max_length) 


solution =Solution()
solution.lengthOfLongestSubstring("abcabcbb")