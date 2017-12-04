class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if not root:
                return 0
            else:
                return max(depth(root.left), depth(root.right)) + 1

        if not root:
            return True
        else:
            return (
                abs(depth(root.left) - depth(root.right)) < 2
                and self.isBalanced(root.left) and
                self.isBalanced(root.right))

a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
a.right = b
b.left = c
s = Solution()
print(s.isBalanced(a))
