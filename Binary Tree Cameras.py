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
        self.count = 0
        self.root = root
        if self.dfs(root) == 0:
            self.count += 1
        return self.count

    def dfs(self, node):
        # no camera 0
        # camera 2
        # no need 1
        if not node:
            return 1
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left == 0 or right == 0:
            # covered
            self.count += 1
            # has camera
            return 2
        if left == 2 or right == 2:
            return 1
        return 0


a = TreeNode(0)
b = TreeNode(0)
c = TreeNode(0)
d = TreeNode(0)
e = TreeNode(0)
f = TreeNode(0)
a.left = b
b.right = c
c.left = d
d.right = e
e.left = f
s = Solution()
print(s.minCameraCover(a))
