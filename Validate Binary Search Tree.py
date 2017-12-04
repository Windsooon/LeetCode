class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p != q:
            return False
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

p = TreeNode(0)
q = TreeNode(0)

s = Solution()
print(s.isSameTree(p, q))
