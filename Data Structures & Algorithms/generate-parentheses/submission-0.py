class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened, closed, path):
            if len(path) == 2 * n:
                res.append(path[:])
                return
            
            if opened < n:
                backtrack(opened + 1, closed, path + '(')
            
            if opened > closed:
                backtrack(opened, closed + 1, path + ')')

        backtrack(0, 0, "")
        return res
