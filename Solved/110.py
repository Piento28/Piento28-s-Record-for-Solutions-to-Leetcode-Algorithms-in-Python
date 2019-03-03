# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDepth(self,node):
        if node==None:
            return 0
        return max(self.getDepth(node.left)+1,self.getDepth(node.right)+1)
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True;
        if abs(self.getDepth(root.left)-self.getDepth(root.right))>1:
            return False
        elif (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        else:
            return False
        