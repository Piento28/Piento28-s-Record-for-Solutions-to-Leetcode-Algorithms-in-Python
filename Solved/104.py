# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive version, more memory space:
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root==None:
#             return 0
#         return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        rec = []
        stack = []
        stack.append([root,1])
        while stack:
            current = stack.pop(-1)
            if current[0].left!=None:
                stack.append([current[0].left,current[1]+1])
            if current[0].right!=None:
                stack.append([current[0].right,current[1]+1])
            # if current[0].left==None and current[0].right==None:
            rec.append(current[1])
        return max(rec)