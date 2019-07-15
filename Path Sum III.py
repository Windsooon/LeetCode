# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.count = 0
        self.dic = {0:1}
        # breakpoint()
        self.dfs(root, 0, sum)
        return self.count

    def dfs(self, node, pre, sum):
        if node.val + pre - sum in self.dic:
            self.count += self.dic[node.val + pre - sum]
        if pre + node.val in self.dic:
            self.dic[pre+node.val] += 1
        else:
            self.dic[pre+node.val] = 1
        for n in (node.left, node.right):
            if n:
                self.dfs(n, pre+node.val, sum)
        self.dic[pre+node.val] -= 1

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
