# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.lis.append(node.val)
        if node.right:
            self.inorder(node.right)
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.lis=[]
        self.inorder(root)
        max_bound = self.lis[0]
        for v in self.lis[1:]:
            print(v)
            if v>max_bound:
                max_bound = v
            else:
                return False
        return True