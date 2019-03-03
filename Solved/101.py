# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None and q!=None:
            return False
        if p!=None and q==None:
            return False
        if p.val!=q.val:
            return False

        if (self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)):
            return True
        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.isSameTree(root.left,root.right)