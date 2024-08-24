class Solution(object):

    def romanToInt(self, s):
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_number = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
                int_number -= roman_numbers[s[i]]
            else:
                int_number += roman_numbers[s[i]]

        print(int_number)


solution = Solution()
solution.romanToInt("MCMXCIV")
