# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        dummy = TreeNode(1)
        breakpoint()
        self.recursion(root, dummy)
        root = dummy.next
        
    def recursion(self, node, pre):
        pre.left = None
        pre.right = node
        current = node
        if node.left:
            tem = node.left
            self.recursion(node.left, current)
            current = tem
        if node.right:
            self.recursion(node.right, current)

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
    z = z.next
