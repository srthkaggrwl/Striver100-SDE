class Solution(object):
    def isValid(self, s):
        
        if not s:
            return
        
        stack = []


        for ch in s:
            try:
                if ch in ['(','[','{']:
                    stack.append(ch)

                elif ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False


                elif ch == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False


                elif ch == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False


                else:
                    continue

            
            except Exception:
                return False


        if len(stack) == 0:
            return True
        else:
            return False



solution = Solution()
print(solution.isValid("()[]{}"))