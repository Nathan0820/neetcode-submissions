class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paradict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in paradict:
                stack.append(c)
            else:
                if not stack or paradict[c] != stack[-1]:
                    return False
                stack.pop()
                
        return not stack