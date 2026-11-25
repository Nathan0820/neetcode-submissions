class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                s, f = stack.pop(), stack.pop()
                if c == "+":
                    stack.append((f + s))
                elif c == "-":
                    stack.append((f - s))
                elif c == "*":
                    stack.append((f * s))
                elif c == "/":
                    stack.append(int(f / s))
        return stack[0]
