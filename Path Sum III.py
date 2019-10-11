# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        breakpoint()
        self.dfs(root, sum)
        return self.count

    def dfs(self, node, sum):
        if not node:
            return
        if sum - node.val == 0:
            self.count += 1
        for child in [node.left, node.right]:
            self.dfs(child, sum-node.val)
            self.dfs(child, sum)

# a = TreeNode(5)
# b = TreeNode(4)
# c = TreeNode(8)
# d = TreeNode(11)
# e = TreeNode(13)
# f = TreeNode(4)
# g = TreeNode(7)
# h = TreeNode(2)
# i = TreeNode(5)
# j = TreeNode(1)
# 
# a.left = b
# a.right = c
# b.left = d
# d.left = g
# d.right = h
# c.left = e
# c.right = f
# f.left = i
# f.right = j
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(-3)
a.left =b
a.right = c
d = TreeNode(3)
e = TreeNode(2)
b.left = d
b.right = e
f = TreeNode(11)
c.right = f
g = TreeNode(3)
h = TreeNode(-2)
d.left = g
d.right = h
i = TreeNode(1)
e.right = i

s = Solution()
print(s.pathSum(a, 8))
