# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack = []
        stack.append([root,0])
        answer = []
        while stack:
            target = stack[-1][0]
            if stack[-1][1]==0 and (target.left or target.right):
                stack[-1][1]=1
                if target.right:
                    stack.append([target.right,0])
                if target.left:
                    stack.append([target.left,0])
                continue
            answer.append(target.val)
            stack.pop(-1)
        return answer