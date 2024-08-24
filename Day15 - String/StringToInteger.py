class Solution(object):
    def myAtoi(self, s):
        temp = ''
        s = s.strip()

        if not s:
            return 0

        sign = 1  # Default to positive sign

        # Handle optional sign at the beginning
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1

        for i in range(start, len(s)):
            if s[i].isdigit():
                temp += s[i]
            else:
                break

        if not temp:  # Handle case where no digits were found
            return 0

        int_number = sign * int(temp)


        int_number = max(min(int_number, 2**31 - 1), -2**31)

        return int_number

solution = Solution()
print(solution.myAtoi("   -001337c0d3"))  
