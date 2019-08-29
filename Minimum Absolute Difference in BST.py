# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.lst = []
        self.inorder(root)
        min_diff = float('inf')
        for i in range(len(self.lst)-1):
            min_diff = min(min_diff, abs(self.lst[i] - self.lst[i+1]))
        return min_diff


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.lst.append(root.val)
        self.inorder(root.right)
