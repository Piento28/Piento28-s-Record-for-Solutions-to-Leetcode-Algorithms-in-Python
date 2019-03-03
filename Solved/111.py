# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# From maxDepth 104
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root==None:
#             return 0
#         rec = []
#         stack = []
#         stack.append([root,1])
#         while stack:
#             current = stack.pop(0)
#             if current[0].left!=None:
#                 stack.append([current[0].left,current[1]+1])
#             if current[0].right!=None:
#                 stack.append([current[0].right,current[1]+1])
#             if current[0].left==None and current[0].right==None:
#                 rec.append(current[1])
#         return min(rec)

# Early Stop Version
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        rec = []
        stack = []
        stack.append([root,1])
        while stack:
            current = stack.pop(0)
            if current[0].left!=None:
                stack.append([current[0].left,current[1]+1])
            if current[0].right!=None:
                stack.append([current[0].right,current[1]+1])
            if current[0].left==None and current[0].right==None:
                rec.append(current[1])
                return min(rec)
