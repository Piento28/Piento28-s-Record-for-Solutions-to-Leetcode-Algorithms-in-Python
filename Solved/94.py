# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, node: TreeNode) -> List[int]:
        if node==None:
            return []
        stack = []
        stack.append(node)
        answer = []
        while stack:
            target = stack[-1]
            while target.left!=None:
                target = target.left
                stack.append(target)
            target = stack.pop(-1)
            answer.append(target.val)
            while target.right==None and stack:
                target = stack.pop(-1)
                answer.append(target.val)
            if target.right:
                stack.append(target.right)
        return answer
    