# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        # curr = root
        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     else: #split happens
        #         return curr
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root 