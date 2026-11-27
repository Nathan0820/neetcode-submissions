# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = max(depth of left) + max(depth of right)
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        

        if not root:
            return 0
        
        throughRoot = maxDepth(root.left) + maxDepth(root.right)
        return max(throughRoot, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))