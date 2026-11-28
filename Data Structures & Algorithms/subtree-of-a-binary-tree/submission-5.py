# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            q = [(p, q)]
            while q:
                l, r = q.pop()

                if not l and not r:
                    continue
                
                if not l or not r or l.val != r.val:
                    return False
                
                q.append((l.left, r.left))
                q.append((l.right, r.right))
            return True

        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
