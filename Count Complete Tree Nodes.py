# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        height = self.get_h(root)
        if not root:
            return 0
        if self.get_h(root.left) == self.get_h(root.right):
            return 2**(height-1) + self.countNodes(root.right)
        else:
            return 2**(height-2) + self.countNodes(root.left)

    def get_h(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
s = Solution()
