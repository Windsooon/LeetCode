# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.max_val = float('-inf')
        self.dfs(root)
        return self.max_val

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_val = max(self.max_val, root.val + left + right)
        return max(root.val, root.val + max(left, right), 0)


a = TreeNode(-10)
b = TreeNode(2)
c = TreeNode(6)
a.left = b
a.right = c

s = Solution()
print(s.maxPathSum(a))
