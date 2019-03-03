# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        if p.val>q.val:
            temp=p
            p=q
            q=tmp
        while True:
            if current.val==p.val:
                return p
            if current.val==q.val:
                return q
            if p.val<current.val and q.val>current.val:
                return current
            if q.val<current.val:
                current=current.left
                continue
            if p.val>current.val:
                current=current.right
                continue
