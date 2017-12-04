# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.right:
            return (
                root.left.val == root.right.val and
                self.isSymmetric(root.left)
                and self.isSymmetric(root.right))
        return root.left is root.right
