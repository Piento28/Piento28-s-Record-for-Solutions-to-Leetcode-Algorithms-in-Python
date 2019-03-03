# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, x: int) -> bool:
        if not root:
            # if x==0:
            #     return F
            # else:
            return False
        if (not root.left) and (not root.right) and (x==root.val):
            return True
        left_result=right_result=False
        if root.left:
            left_result = self.hasPathSum(root.left,x-root.val)
        if root.right:
            right_result = self.hasPathSum(root.right,x-root.val)
        return left_result or right_result

