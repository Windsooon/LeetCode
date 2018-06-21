# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res, strings = [], ''
        if not root:
            return
        self.helper(root, strings, res)
        return res

    def helper(self, root, strings, res):
        if not root.left and not root.right:
            res.append(strings+str(root.val))
        if root.left:
            self.helper(root.left, strings+str(root.val)+'->', res)
        if root.right:
            self.helper(root.right, strings+str(root.val)+'->', res)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left = b
a.right = c
b.right = d

s = Solution()
print(s.binaryTreePaths(a))
