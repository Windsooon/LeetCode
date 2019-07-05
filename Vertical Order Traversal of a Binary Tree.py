# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import PriorityQueue
class Solution:
    def verticalTraversal(self, root):
        # edge case
        pass

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e


s = Solution()
print(s.verticalTraversal(a))
