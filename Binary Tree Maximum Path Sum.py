# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_sum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            return root.val + max(max_sum(root.left), max_sum(root.right), 0)

        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        return max(
            root.val,
            max_sum(root.left), max_sum(root.right),
            max_sum(root.left) + root.val + max_sum(root.right))


class Solution(object):
    def __init__(self):
        self.max = float('-inf')

    def maxPathSum(self, root):
        self.recursion(root)
        return self.max

    def recursion(self, node):
        if not node:
            return 0
        left = self.recursion(node.left)
        right = self.recursion(node.right)
        self.max = max(self.max, left + node.val + right)
        return max(node.val + max(left, right), 0)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(-3)
a.left = b
a.right = c

s = Solution()
print(s.maxPathSum(a))
