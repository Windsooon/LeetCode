# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    length = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0
            left, right = helper(root.left), helper(root.right)
            self.length = max(self.length, left + right)
            return max(helper(root.left), helper(root.right)) + 1
        helper(root)
        return self.length


a = TreeNode(5)
a.left = TreeNode(5)
a.right = TreeNode(5)
a.right.right = TreeNode(5)
a.right.right.left = TreeNode(5)
a.left.left = TreeNode(5)
a.left.right = TreeNode(1)

s = Solution()
print(s.diameterOfBinaryTree(a))
