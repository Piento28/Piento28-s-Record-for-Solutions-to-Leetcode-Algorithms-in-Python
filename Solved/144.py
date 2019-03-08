# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack = []
        answer = []
        stack.append(root)
        while stack:
            target = stack.pop(-1)
            answer.append(target.val)
            if target.right!=None:
                stack.append(target.right)
            if target.left!=None:
                stack.append(target.left)
        return answer