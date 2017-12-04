class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        def sum(node, value):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            if root.left:
                

        sum(root, 0)

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
print(s.sumNumbers(a))
