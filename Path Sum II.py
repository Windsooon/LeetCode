# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        if root.val == sum and not root.left and not root.right:
            return [[root.val]]
        return self.dfs(root, [], root.val, sum, [root.val])

    def dfs(self, node, res, current, target, path):
        for n in [node.left, node.right]:
            if self.is_valid(n):
                if current + n.val == target and not n.left and not n.right:
                    tem = path[:]
                    tem.append(n.val)
                    res.append(tem)
                else:
                    self.dfs(n, res, current+n.val, target, path+[n.val])
        return res

    def is_valid(self, node):
        if node:
            return True
        return False

a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(5)
j = TreeNode(1)

a.left = b
a.right = c
b.left = d
d.left = g
d.right = h
c.left = e
c.right = f
f.left = i
f.right = j


s = Solution()
print(s.pathSum(a, 22))
