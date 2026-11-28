# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 1

        def dfs(node, val):
            if not node:
                return 
            val = max(val, node.val)
            if node.left and node.left.val >= val:
                self.res += 1
            if node.right and node.right.val >= val:
                self.res += 1
            dfs(node.left, val)
            dfs(node.right, val)
        
        dfs(root, root.val)
        return self.res
