import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = collections.deque()
        results = []
        if not root:
            return []
        d.append(root)
        while d:
            k = d.popleft()
            results.append(k.val)
            if k.left:
                d.append(k.left)
            if k.right:
                d.append(k.right)
        return results

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

s = Solution()
print(s.levelOrder(a))
