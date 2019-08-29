# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.current = 0
        self.greater(root)
        return root

    def greater(self, root):
        if not root:
            return
        self.greater(root.right)
        root.val += self.current
        self.current = root.val
        self.greater(root.left)


# class Solution(object):
#     def convertBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         breakpoint()
#         self.cur_sum = 0
#         self.convertHelper(root)
#         return root
# 
#     def convertHelper(self, root):
#         if not root:
#             return
#         self.convertHelper(root.right)
#         root.val += self.cur_sum
#         self.cur_sum = root.val
#         self.convertHelper(root.left)

a = TreeNode(2)
b = TreeNode(5)
c = TreeNode(13)
b.left = a
b.right = c

s = Solution()
s.convertBST(b)
