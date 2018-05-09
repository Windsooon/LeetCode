# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if the tree is empty
        self.smallest = float('-inf')

        # inorder for in the tree
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.smallest:
                ans = False
            else:
                self.smallest = root.val
                ans = True
            if not inorder(root.right):
                return False
            return ans
        return inorder(root)


a = TreeNode(1)
b = TreeNode(1)
b.left = a

s = Solution()
print(s.isValidBST(b))
