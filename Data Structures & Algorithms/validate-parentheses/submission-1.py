class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)

            if c == ')':
                if len(stack) < 1:
                    return False

                x = stack.pop()
                if x != '(':
                    return False

            if c == '}':
                if len(stack) < 1:
                    return False
                x = stack.pop()
                if x != '{':
                    return False
            
            if c == ']':
                if len(stack) < 1:
                    return False
                x = stack.pop()
                if x != '[':
                    return False

        if len(stack) != 0:
            return False
        return True