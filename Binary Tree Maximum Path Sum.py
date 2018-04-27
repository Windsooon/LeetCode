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

a = TreeNode(2)
b = TreeNode(-1)
a.left = b

s = Solution()
print(s.maxPathSum(a))
