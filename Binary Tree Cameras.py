# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root):
        if not root:
            return 0
        return min(self.dfs(root), self.dfs(root.left)+self.dfs(root.right))

    def dfs(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        if node.left and node.right:
            return 1+self.dfs(node.left.left)+self.dfs(node.left.right)+self.dfs(node.right.left)+self.dfs(node.right.right)
        if node.left:
            return 1+self.dfs(node.left.left)+self.dfs(node.left.right)
        if node.right:
            return 1+self.dfs(node.right.left)+self.dfs(node.right.right)


a = TreeNode(0)
b = TreeNode(0)
c = TreeNode(0)
d = TreeNode(0)
e = TreeNode(0)
a.left = b
b.left = c
c.left = d
d.left = e
s = Solution()
print(s.minCameraCover(a))
