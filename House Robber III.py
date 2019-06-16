# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        if not root:
            return 0
        return self.dp(root)[0]

    def dp(self, node):
        if not node:
            # for a nonexist node
            return 0, 0
        if not node.left and not node.right:
            # for a leaf node
            return node.val, 0
        # return sum of child for speed up
        left, lchild = self.dp(node.left)
        right, rchild = self.dp(node.right)
        return max(left+right, node.val+lchild+rchild), left+right


a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(1)
a.left = b
a.right = c
b.right = d
c.right = e
# a = TreeNode(3)
# b = TreeNode(4)
# c = TreeNode(5)
# d = TreeNode(1)
# e = TreeNode(3)
# f = TreeNode(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

s = Solution()
print(s.rob(a))
