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
        :rtype: void Do not return anything, modify root in-place instead.
        """
        ans, s = root, []
        while root or s:
            if root:
                s.append(root)
                if root.left:
                    root.next = root.left
                root = root.left
            else:
                root = s.pop()
                if root.right:
                    root.next = root.right
                root = root.right
        return ans

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
