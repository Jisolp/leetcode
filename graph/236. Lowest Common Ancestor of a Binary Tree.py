# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root: return None

        # if root == p or root == q:
        #     return root

        # l = self.lowestCommonAncestor(root.left, p,q)
        # r = self.lowestCommonAncestor(root.right,p,q)

        # if l and r:
        #     return root
        # else:
        #     return l or r
        if not root: return None

        def dfs(curr):
            if curr == p or curr == q:
                return curr
            if (curr):
                l = dfs(curr.left)
                r = dfs(curr.right)
                if l and r:
                    return curr
                else:
                    return l or r
        return dfs(root)
