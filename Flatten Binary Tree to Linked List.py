# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        dummy = pre = TreeNode(0)
        while root:
            pre.left = 
            pre.right = root
            if root.left:
                node = self.find_rightmost(root.left)
                node.right = root.right
                pre = root
                root = root.left
            else:
                pre = root
                root = root.right
        return dummy.right
    
    def find_rightmost(self, node):
        while node.right:
            node = node.right
        return node

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left = b
a.right = e
b.left = c
b.right = d
e.right = f

s = Solution()
z = s.flatten(a)
while z:
    print(z.val)
    z = z.right
